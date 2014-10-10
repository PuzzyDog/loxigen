# Copyright 2013, Big Switch Networks, Inc.
#
# LoxiGen is licensed under the Eclipse Public License, version 1.0 (EPL), with
# the following special exception:
#
# LOXI Exception
#
# As a special exception to the terms of the EPL, you may distribute libraries
# generated by LoxiGen (LoxiGen Libraries) under the terms of your choice, provided
# that copyright and licensing notices generated by LoxiGen are not altered or removed
# from the LoxiGen Libraries and the notice provided below is (i) included in
# the LoxiGen Libraries, if distributed in source code form and (ii) included in any
# documentation for the LoxiGen Libraries, if distributed in binary form.
#
# Notice: "Copyright 2013, Big Switch Networks, Inc. This library was generated by the LoxiGen Compiler."
#
# You may not use this file except in compliance with the EPL or LOXI Exception. You may obtain
# a copy of the EPL at:
#
# http://www.eclipse.org/legal/epl-v10.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# EPL for the specific language governing permissions and limitations
# under the EPL.

"""
Python backend for LOXI

Target directory structure:
    pyloxi:
        loxi:
            __init__.py
            of10:
                __init__.py
                action.py       # Action classes
                common.py       # Structs shared by multiple messages
                const.py        # OpenFlow constants
                message.py      # Message classes
                util.py         # Utility functions
            of11: ...           # (code generation incomplete)
                instruction.py  # Instruction classes
            of12: ...           # (code generation incomplete)
                oxm.py          # OXM classes
            of13: ...           # (code generation incomplete)
                action_id.py    # Action ID classes
                instruction_id.py # Instruction ID classes
                meter_band.py   # Meter band classes

The user will add the pyloxi directory to PYTHONPATH. Then they can
"import loxi" or "import loxi.of10". The idiomatic import is
"import loxi.of10 as ofp". The protocol modules (e.g. of10) import
all of their submodules, so the user can access "ofp.message" without
further imports. The protocol modules also import the constants from
the const module directly into their namespace so the user can access
"ofp.OFPP_NONE".
"""

import os
import py_gen.codegen

PREFIX = 'pyloxi/loxi'

def generate(install_dir):
    py_gen.codegen.codegen(os.path.join(install_dir, PREFIX))
