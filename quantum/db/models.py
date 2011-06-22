# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Copyright 2011 Nicira Networks, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
# @author: Somik Behera, Nicira Networks, Inc.
# @author: Brad Hall, Nicira Networks, Inc.
# @author: Dan Wendlandt, Nicira Networks, Inc.

import uuid

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation

BASE = declarative_base()


class Port(BASE):
    """Represents a port on a quantum network"""
    __tablename__ = 'ports'

    uuid = Column(String(255), primary_key=True)
    network_id = Column(String(255), ForeignKey("networks.uuid"),
                        nullable=False)
    interface_id = Column(String(255))

    def __init__(self, network_id):
        self.uuid = uuid.uuid4()
        self.network_id = network_id

    def __repr__(self):
        return "<Port(%s,%s,%s)>" % (self.uuid, self.network_id,
                                     self.interface_id)


class Network(BASE):
    """Represents a quantum network"""
    __tablename__ = 'networks'

    uuid = Column(String(255), primary_key=True)
    tenant_id = Column(String(255), nullable=False)
    name = Column(String(255))
    ports = relation(Port, order_by=Port.uuid, backref="network")

    def __init__(self, tenant_id, name):
        self.uuid = uuid.uuid4()
        self.tenant_id = tenant_id
        self.name = name

    def __repr__(self):
        return "<Network(%s,%s,%s)>" % \
          (self.uuid, self.name, self.tenant_id)
