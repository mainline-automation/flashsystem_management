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
    vol_base_name:
        description: This is the volume base name provided
        required: true
        type: str
    vol_sequence_begin:
        description: This is the volume sequence number to be added
        required: true
        type: int
    vol_sequence_end:
        description: This is the volume sequence number to be added
        required: true
        type: int
    vol_sequence_increment:
        description: This is the amount to increase the sequence number by
        required: false
        type: int
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
# extends_documentation_fragment:
#     - my_namespace.my_collection.my_doc_fragment_name

author:
    - Ian Wright (@steeltalon)
'''
RETURN = r'''
# The only important return value is vol_names
vol_names:
    description: The new volume name
    type: list
    returned: always
    sample: 'new1
             new2'

'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    # parameters provided by user in ansible
    module_args = dict(
        vol_base_name=dict(type='str', required=True),
        vol_sequence_begin=dict(type='int', required=True),
        vol_total=dict(type='int', required=True, ),
        vol_sequence_increment=dict(type='int', default=True)
    )

    # result['vol_names'] starts off as a blank list in the dictionary
    result = dict(
        changed=False,
        vol_names=[]
    )

    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # check mode is provided
    # if module.check_mode:
    #     module.exit_json(**result)

    # Loop from beginning number to end number by increment. Default increment is 1

    if module.params['vol_sequence_increment'] <= 0:
        module.params['vol_sequence_increment'] == 1
    
    vol_sequence_end = module.params['vol_sequence_begin'] + ((module.params['vol_sequence_increment'] - 1) * module.params['vol_total'])
    for vol_sequence_number in range (module.params['vol_sequence_begin'], ((vol_sequence_end + 1), module.params['vol_sequence_increment'])):
        result['vol_names'].append(module.params['vol_base_name'] +'_'+ str(vol_sequence_number))
    # determines that input parameters were provided and changed
    if result['vol_names'] != []:
        result['changed'] = True

    #Logic to validate that input was provided
    if module.params['vol_base_name'] == '':
        module.fail_json(msg='Provide a volume base name', **result)
    else:
        if module.params['vol_sequence_begin'] == '':
           module.fail_json(msg='Provide a volume sequence begin number', **result)
        else:
            if module.params['vol_sequence_end'] == '':
                module.fail_json(msg='Provide a volume sequence ending number', **result)

    # module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()