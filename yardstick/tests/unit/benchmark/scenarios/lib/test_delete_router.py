##############################################################################
# Copyright (c) 2017 Huawei Technologies Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################
import unittest
import mock

from yardstick.benchmark.scenarios.lib.delete_router import DeleteRouter


class DeleteRouterTestCase(unittest.TestCase):

    @mock.patch('yardstick.common.openstack_utils.get_neutron_client')
    @mock.patch('yardstick.common.openstack_utils.delete_neutron_router')
    def test_delete_router(self, mock_get_neutron_client, mock_delete_neutron_router):
        options = {
            'router_id': '123-123-123'
        }
        args = {"options": options}
        obj = DeleteRouter(args, {})
        obj.run({})
        self.assertTrue(mock_get_neutron_client.called)
        self.assertTrue(mock_delete_neutron_router.called)


def main():
    unittest.main()


if __name__ == '__main__':
    main()