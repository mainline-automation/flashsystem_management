#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import,division, print_function)
__metaclass__ = type
DOCUMENTATION = r'''
---
module: create_volume_name

version_added: "1.0.0"

short description: This module will create a volume name from the base name and the sequence number

description: Ansible on its own won't merge a list value with a str or int. This module will do that by converting the values appropriately

options:
    svc_info_results:
        description: This is the list from ibm.svc_info
        required: true
        type: list
    info_value:
        description: The value that needs to be extracted for the survey list
        required: true
        type: str
    
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
# extends_documentation_fragment:
#     - my_namespace.my_collection.my_doc_fragment_name

author:
    - Ian Wright (@steeltalon)
'''
RETURN = r'''
# The only important return value is vol_names
survey_list:
    description: The properly formatted list 
    type: list
    returned: always
    sample: ['pool1', 'pool2',...]

'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    # parameters provided by user in ansible
    # module_args = dict(
    #     svc_info_results=dict(type='list', required=True),
    #     info_value=dict(type=str, required=True)
    

    # simplified variables
    # svc_info_results = module_args['svc_info_results']
    # info_value=module_args['info_value']

    # survey list starts off as a blank list in the dictionary
    svc_info_results= [
                       {
                                "capacity": "0",
                                "child_mdisk_grp_capacity": "0.00MB",
                                "child_mdisk_grp_count": "0",
                                "compression_active": "no",
                                "compression_compressed_capacity": "0.00MB",
                                "compression_uncompressed_capacity": "0.00MB",
                                "compression_virtual_capacity": "0.00MB",
                                "data_reduction": "yes",
                                "deduplication_capacity_saving": "0.00MB",
                                "easy_tier": "auto",
                                "easy_tier_fcm_over_allocation_max": "",
                                "easy_tier_status": "balanced",
                                "encrypt": "",
                                "extent_size": "4096",
                                "free_capacity": "0",
                                "id": "0",
                                "mdisk_count": "0",
                                "name": "TestDDRPool",
                                "overallocation": "0",
                                "overhead_capacity": "0.00MB",
                                "owner_id": "",
                                "owner_name": "",
                                "owner_type": "none",
                                "parent_mdisk_grp_id": "0",
                                "parent_mdisk_grp_name": "TestDDRPool",
                                "provisioning_policy_id": "",
                                "provisioning_policy_name": "",
                                "real_capacity": "0.00MB",
                                "reclaimable_capacity": "0.00MB",
                                "site_id": "",
                                "site_name": "",
                                "status": "online",
                                "type": "parent",
                                "used_capacity": "0.00MB",
                                "used_capacity_after_reduction": "0.00MB",
                                "used_capacity_before_reduction": "0.00MB",
                                "vdisk_count": "0",
                                "virtual_capacity": "0.00MB",
                                "warning": "80"
                            },
                            {
                                "capacity": "0",
                                "child_mdisk_grp_capacity": "0.00MB",
                                "child_mdisk_grp_count": "0",
                                "compression_active": "no",
                                "compression_compressed_capacity": "0.00MB",
                                "compression_uncompressed_capacity": "0.00MB",
                                "compression_virtual_capacity": "0.00MB",
                                "data_reduction": "yes",
                                "deduplication_capacity_saving": "0.00MB",
                                "easy_tier": "auto",
                                "easy_tier_fcm_over_allocation_max": "",
                                "easy_tier_status": "balanced",
                                "encrypt": "",
                                "extent_size": "4096",
                                "free_capacity": "0",
                                "id": "1",
                                "mdisk_count": "0",
                                "name": "TestSSPCTest",
                                "overallocation": "0",
                                "overhead_capacity": "0.00MB",
                                "owner_id": "",
                                "owner_name": "",
                                "owner_type": "none",
                                "parent_mdisk_grp_id": "1",
                                "parent_mdisk_grp_name": "TestSSPCTest",
                                "provisioning_policy_id": "",
                                "provisioning_policy_name": "",
                                "real_capacity": "0.00MB",
                                "reclaimable_capacity": "0.00MB",
                                "site_id": "",
                                "site_name": "",
                                "status": "online",
                                "type": "parent",
                                "used_capacity": "0.00MB",
                                "used_capacity_after_reduction": "0.00MB",
                                "used_capacity_before_reduction": "0.00MB",
                                "vdisk_count": "0",
                                "virtual_capacity": "0.00MB",
                                "warning": "80"
                            },
                            {
                                "capacity": "99.01TB",
                                "child_mdisk_grp_capacity": "0.00MB",
                                "child_mdisk_grp_count": "0",
                                "compression_active": "no",
                                "compression_compressed_capacity": "0.00MB",
                                "compression_uncompressed_capacity": "0.00MB",
                                "compression_virtual_capacity": "0.00MB",
                                "data_reduction": "no",
                                "deduplication_capacity_saving": "0.00MB",
                                "easy_tier": "auto",
                                "easy_tier_fcm_over_allocation_max": "",
                                "easy_tier_status": "balanced",
                                "encrypt": "no",
                                "extent_size": "1024",
                                "free_capacity": "71.96TB",
                                "id": "2",
                                "mdisk_count": "1",
                                "name": "Pool_01",
                                "overallocation": "27",
                                "overhead_capacity": "0.00MB",
                                "owner_id": "",
                                "owner_name": "",
                                "owner_type": "none",
                                "parent_mdisk_grp_id": "2",
                                "parent_mdisk_grp_name": "Pool_01",
                                "provisioning_policy_id": "",
                                "provisioning_policy_name": "",
                                "real_capacity": "27.04TB",
                                "reclaimable_capacity": "0.00MB",
                                "site_id": "",
                                "site_name": "",
                                "status": "online",
                                "type": "parent",
                                "used_capacity": "27.03TB",
                                "used_capacity_after_reduction": "0.00MB",
                                "used_capacity_before_reduction": "0.00MB",
                                "vdisk_count": "12",
                                "virtual_capacity": "27.33TB",
                                "warning": "80"
                            }
                        ]
    
    info_value = 'name'
    result = dict(
        changed=False,
        survey_list=[]
    )

    # supports check mode
    # module = AnsibleModule(
    #     argument_spec=module_args,
    #     supports_check_mode=True
   

    # # check mode is provided
    # if module.check_mode:
    #     module.exit_json(**result)

    # Loop from beginning number to end number by increment. Default increment is 1
    x=0
    while x < len(svc_info_results):
        if x < len(svc_info_results):
            result['survey_list'].append(svc_info_results[x][info_value],)
            x = x+1
        
    # determines that input parameters were provided and changed
    
    
    if result['survey_list'] != []:
        result['changed'] = True
    print (result['survey_list'])

    #Logic to validate that input was provided
    
    
    

    # module.exit_json(**result)


def main():
    run_module()
    


if __name__ == '__main__':
    main()