#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import,division, print_function)
__metaclass__ = type
DOCUMENTATION = r'''
---
module: create_survey_info

version_added: "1.0.0"

short description: This module will create a volume name from the base name and the sequence number

description: Ansible on its own won't merge a list value with a str or int. This module will do that by converting the values appropriately and formats into a list of dictionaries

options:
    info_results:
        description: This is the list from module gathering info
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
survey_info:
    description: The properly formatted list of dictionaries
    type: list
    returned: always
    sample: ['name': 'pool1', 'name': 'pool2',...]

'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    # parameters provided by user in ansible
    module_args = dict(
        info_results=dict(type='list', required=True),
        info_value=dict(type=str, required=True)
    )

    # survey list starts off as a blank list in the dictionary
    result = dict(
        changed=False,
        survey_info=[]
    )

    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # check mode is provided
    if module.check_mode:
        module.exit_json(**result)

    # Loop from beginning number to end number by increment. Default increment is 1
    x=0
    requested_value={}
    while x < len(module.params['info_results']):
        if x < len(module.params['info_results']):
            requested_value[x] = result['survey_info'].append(module.params['info_results'][x][module.params['info_value']],)
            x = x+1
    # remove duplicate values
    result['survey_info'] = list(dict.fromkeys(result['survey_info']))
        
    # determines that input parameters were provided and changed
    
    
    if result['survey_info'] != []:
        result['changed'] = True

    #Logic to validate that input was provided
    
    
    

    module.exit_json(**result)

def new_func(module):
    print(module.params['info_results'])


def main():
    run_module()


if __name__ == '__main__':
    main()