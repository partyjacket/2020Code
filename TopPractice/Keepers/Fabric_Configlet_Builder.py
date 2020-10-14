# Author: Jason Patterson - jpatterson@arista.com
#
#!/usr/bin/python

from jsonrpclib import Server
from cvplibrary import Form
from cvplibrary import CVPGlobalVariables,GlobalVariableNames
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
#
# Get all data from Form
spine1_port_num = Form.getFieldById('spine1_port_num').getValue()
spine2_port_num = Form.getFieldById('spine2_port_num').getValue()
spine3_port_num = Form.getFieldById('spine3_port_num').getValue()



ip = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_IP)
myCVPuser = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_USERNAME)
myCVPpasswd = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_PASSWORD)

#
# Username/password/protocol for eAPI access to switches
#

EAPI_USERNAME = myCVPuser
EAPI_PASSWORD = myCVPpasswd
EAPI_METHOD = 'https'

#
# Via eAPI call get detect unique loopback ip address use to derive fabric interfaces
##!!Changing "unique_loopback_ip to call loopback0 for Jasons Lab!!"
switch = Server( '%s://%s:%s@%s/command-api' % ( EAPI_METHOD, EAPI_USERNAME, EAPI_PASSWORD, ip ) )

unique_loopback_ip = switch.runCmds(1, ['show ip interface loopback0'])[0]['interfaces']['Loopback0']['interfaceAddress']['primaryIp']['address']
vtep_octet = unique_loopback_ip.split('.')[2]
node_octet = unique_loopback_ip.split('.')[-1]

# BASE CONFIG TEMPLATE

iface_base_config = '   mtu 9214\n' \
                    '   no switchport\n'

# Fabric Iface Description
desc = '   description '
iface_49_desc = desc + 'b10cmr0-spine1_eth{}\n'.format(spine1_port_num)
iface_50_desc = desc + 'b10cmr0-spine2_eth{}\n'.format(spine2_port_num)
iface_51_desc = desc + 'b11cmr0-spine3_eth{}\n'.format(spine3_port_num)


# Template IP addresses
underlay_base_ip = {
    'spine1': '10.241.',
    'spine2': '10.242.',
    'spine3': '10.243.'
}

underlay_leaf_ip = {
    'leafa': '2',
    'leafb': '6'
}

underlay_spine_ip = {
    'leafa': '1',
    'leafb': '5'
}

underlay_ibgp_ip = {
    'leafa': '192.168.0.1',
    'leafb': '192.168.0.2'
}

evpn_spine_ip = {
    'spine1': '10.250.0.1',
    'spine2': '10.250.0.2',
    'spine3': '10.250.0.3'
}
# UNDERLAY INTERFACE CONFIG

def iface_underlay_ip():
    link_ip_dict = {}
    if node_octet == '1':
        for i in range(1, 4):
            link_ip_dict['link{}_ip'.format(i)] = underlay_base_ip['spine{}'.format(i)] \
                                                  + vtep_octet + '.' + underlay_leaf_ip.get('leafa')

    elif node_octet == '2':
        for i in range(1, 4):
            link_ip_dict['link{}_ip'.format(i)] = underlay_base_ip['spine{}'.format(i)] \
                                                  + vtep_octet + '.' + underlay_leaf_ip.get('leafb')
    return link_ip_dict

def iface_underlay_config():
    iface_underlay_ip()
    print 'interface 49/1 \n' + iface_49_desc + iface_base_config + '   ip address {}/30 \n!'.format(iface_underlay_ip()['link1_ip'])
    print 'interface 51/1 \n' + iface_50_desc + iface_base_config + '   ip address {}/30 \n!'.format(iface_underlay_ip()['link2_ip'])
    print 'interface 53/1 \n' + iface_51_desc + iface_base_config + '   ip address {}/30 \n!'.format(iface_underlay_ip()['link3_ip'])



iface_underlay_config()

# BGP CONFIG

# Get BGP neighbors

def bgp_neighbors():
    bgp_neighbor_dict = {}
    if node_octet == '1':
        for i in range(1, 4):
            bgp_neighbor_dict['neighbor_spine{}'.format(i)] = underlay_base_ip['spine{}'.format(i)] + vtep_octet + '.' + underlay_spine_ip.get('leafa')

    elif node_octet == '2':
        for i in range(1, 4):
            bgp_neighbor_dict['neighbor_spine{}'.format(i)] = underlay_base_ip['spine{}'.format(i)] + vtep_octet + '.' + underlay_spine_ip.get('leafb')
    return bgp_neighbor_dict

# BGP Underlay Configuration

# Get ASN
def asn():
    asn_base = '65'
    if len(vtep_octet) == 1:
        return asn_base + '00' + vtep_octet
    elif len(vtep_octet) == 2:
        return asn_base + '65' + '0' + vtep_octet
    else:
        return asn_base + '65' + vtep_octet


bgp_underlay_config_list = [
    'router bgp {}'.format(asn()),
    '   router-id {}'.format(unique_loopback_ip),
    '   update wait-install',
    '   no bgp default ipv4-unicast',
    '   maximum-paths 3',
    '   neighbor EVPN-OVERLAY-PEERS peer-group',
    '   neighbor EVPN-OVERLAY-PEERS remote-as 65000',
    '   neighbor EVPN-OVERLAY-PEERS update-source Loopback1',
    '   neighbor EVPN-OVERLAY-PEERS fall-over bfd',
    '   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3',
    '   neighbor EVPN-OVERLAY-PEERS send-community',
    '   neighbor EVPN-OVERLAY-PEERS maximum-routes 0',
    '   neighbor MLAG-PEER peer-group',
    '   neighbor MLAG-PEER remote-as {}'.format(asn()),
    '   neighbor MLAG-PEER next-hop-self',
    '   neighbor MLAG-PEER send-community',
    '   neighbor MLAG-PEER maximum-routes 12000',
    '   neighbor UNDERLAY-PEERS peer-group',
    '   neighbor UNDERLAY-PEERS remote-as 65000',
    '   neighbor UNDERLAY-PEERS send-community',
    '   neighbor UNDERLAY-PEERS maximum-routes 12000',
    '   neighbor {} peer-group UNDERLAY-PEERS'.format(bgp_neighbors()['neighbor_spine1']),
    '   neighbor {} peer-group UNDERLAY-PEERS'.format(bgp_neighbors()['neighbor_spine2']),
    '   neighbor {} peer-group UNDERLAY-PEERS'.format(bgp_neighbors()['neighbor_spine3']),
    '   neighbor {} peer-group EVPN-OVERLAY-PEERS'.format(evpn_spine_ip['spine1']),
    '   neighbor {} peer-group EVPN-OVERLAY-PEERS'.format(evpn_spine_ip['spine2']),
    '   neighbor {} peer-group EVPN-OVERLAY-PEERS'.format(evpn_spine_ip['spine3']),
    '   neighbor {} peer-group MLAG-PEER'.format(underlay_ibgp_ip['leafa'] if node_octet == '2' else underlay_ibgp_ip['leafb']),
    '   redistribute connected route-map RM-CON-TO-BGP',
    '   !',
    '   vlan-aware-bundle Micron',
    '       rd {}:1'.format(unique_loopback_ip),
    '       route-target both 1:1',
    '       redistribute learned',
    '       vlan 1-4000',
    '   !',
    '   address-family evpn',
    '       neighbor EVPN-OVERLAY-PEERS activate',
    '   !',
    '   address-family ipv4',
    '       neighbor MLAG-PEER activate',
    '       neighbor UNDERLAY-PEERS activate']



def build_bgp_underlay_config(*args):
    for arg in args:
        print arg


build_bgp_underlay_config(*bgp_underlay_config_list)