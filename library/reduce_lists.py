#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import,division, print_function)
__metaclass__ = type
DOCUMENTATION = r'''
---
module: reduce_lists

version_added: "1.0.0"

short description: This module will create a volume name from the base name and the sequence number

description: Ansible on its own won't merge a list value with a str or int. This module will do that by converting the values appropriately and formats into a list of dictionaries

options:
    list_to_remove:
        description: This list has the items that will be removed
        required: true
        type: list
    main_list:
        description: This is the larger list from which the other items will be removed
        required: true
        type: list
    
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
# extends_documentation_fragment:
#     - my_namespace.my_collection.my_doc_fragment_name

author:
    - Ian Wright (@steeltalon)
'''
RETURN = r'''
# The only important return value is vol_names
reduced_list:
    description: The list that contains only the items that should be kept
    type: list
    returned: always
    sample: ['name': 'pool1', 'name': 'pool2',...]

'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    # parameters provided by user in ansible
    module_args = dict(
        list_to_remove=dict(type='list', required=True),
        main_list=dict(type='list', required=True)
    )

    # reduced_list starts off as a blank list in the dictionary
    result = dict(
        changed=False,
        reduced_list=[]
    )

    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # check mode is provided
    if module.check_mode:
        module.exit_json(**result)

    # use sets to create a reduced list
    
    result['reduced_list']=set(module.params['main_list']).difference(module.params['list_to_remove'])
    
        
    # determines that input parameters were provided and changed
    
    
    if result['reduced_list'] != []:
        result['changed'] = True

    #Logic to validate that input was provided
    
    
    

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()