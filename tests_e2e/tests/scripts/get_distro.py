#!/usr/bin/env pypy3

# Microsoft Azure Linux Agent
#
# Copyright 2018 Microsoft Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Prints the distro and version of the machine
#

import sys

from azurelinuxagent.common.version import get_distro


def main():
    # Prints '<distro>_<version>'
    # For Azure Container Linux (ACL), return 'acl_<version>' to distinguish it from regular Azure Linux.
    distro = get_distro()
    distro_name = distro[0]
    full_name = distro[3] if len(distro) > 3 else ""
    if "azure container linux" in full_name.lower():
        distro_name = "acl"
    print(distro_name + "_" + distro[1].replace('.', ''))
    sys.exit(0)


if __name__ == "__main__":
    main()
