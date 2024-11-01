# Recheck files
from rich.console import Console
from rich.table import Table
from typing import Literal
import os
import pkg_resources
import sys
import json
import time
import ast

modes = Literal [ 'in_front_of', 'on_call', 'equals_with' ]
licenses_ = Literal [ 'MIT', 'Apache', 'BSD', 'Unlicense', 'Zlib' ]
licenses_list = [ 'MIT', 'Apache', 'BSD', 'Unlicense', 'Zlib' ]

def getWorker() -> str:
    path = os.getcwd()

    if "/" in path:
        return path.split("/")[-1]
    elif "\\" in path:
        return path.split("\\")[-1]
    else:return path

def getImportedModules(file_path) -> list:
    with open(file_path, 'r') as file:
        node = ast.parse(file.read(), filename=file_path)
    
    imports = set()
    for elem in ast.walk(node):
        if isinstance(elem, ast.Import):
            for alias in elem.names:
                imports.add(alias.name)
        elif isinstance(elem, ast.ImportFrom):
            imports.add(elem.module)
    
    return list(imports)

# def handleAllFiles()

class Licenses(object):
    def __init__(self):
        self.mit_license = """Copyright {} {}

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

        self.apache_license = """
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   Copyright {} {}

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License."""
        
        self.bsd_license = """Copyright (c) {} {}. All rights reserved.

Redistribution and use in source and binary forms are permitted provided that the above copyright notice and this paragraph are duplicated in all such forms and that any documentation, advertising materials, and other materials related to such distribution and use acknowledge that the software was developed by the {}. The name of the {} may not be used to endorse or promote products derived from this software without specific prior written permission. THIS SOFTWARE IS PROVIDED `'AS IS″ AND WITHOUT ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, WITHOUT LIMITATION, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE."""

        self.Unlicense = """This is free and unencumbered software released into the public domain.

Author(s): {}
Year: {}

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>"""

        self.zlib_license = """Copyright (c) {} {}

This software is provided 'as-is', without any express or implied
warranty. In no event will the authors be held liable for any damages
arising from the use of this software.

Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it
freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not
   claim that you wrote the original software. If you use this software
   in a product, an acknowledgment in the product documentation would be
   appreciated but is not required.
2. Altered source versions must be plainly marked as such, and must not be
   misrepresented as being the original software.
3. This notice may not be removed or altered from any source distribution."""

    def create(
        self,
        license: licenses_ = "MIT",
        **kwargs
    ) -> str:
        
        if license == "MIT":return self.mit_license.format(kwargs.get("name"), kwargs.get("year"))
        elif license == "Apache":return self.apache_license.format(kwargs.get("name"), kwargs.get("year"))
        elif license == "BSD":return self.bsd_license.format(kwargs.get("name"), kwargs.get("year"), kwargs.get("name"), kwargs.get("name"))
        elif license == "Unlicense":return self.Unlicense.format(kwargs.get("name"), kwargs.get("year"))
        elif license == "Zlib":return self.zlib_license.format(kwargs.get("name"), kwargs.get("year"))
        else:return "<Unkown License>"

class BufferList(object):
    def __init__(self,
                 List: list = [],
                 ):
        
        self.list = List
        
    def parse(self):
        bfd = {}

        for i in range(len(self.list)):
            bfd[str(i+1)] = self.list[i]

        return bfd

    def isexists(self, target):
        if target in self.list:
            return True
        else:return False

    def isinfrontof(self, target, indexes):
        isit = False

        if target in self.list:
            try:
                indx = self.list.index(target)
                if indx == indexes:
                    isit = True
                else:isit = False
            except Exception as e:return e
        
        return isit
    
    def indexexists(self, target):
        if target in self.list:
            return self.list.index(target)
        else:return False

class Things(object):
    def __init__(self) -> None:
        self.def_attrs = ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

    def __str__(self) -> str:
        return json.dumps(dir(self), indent=2)
    
    @property
    def options(self) -> list:
        opts = []

        for item in dir(self):
            if item.startswith("__") and item in self.def_attrs:pass
            else:opts.append(item)

        opts.remove("def_attrs")
        opts.remove("options")
        
        return opts

class BufferConsole(object):
    def __init__(self):
        self.last_things = Things()
        self.handlers = []
        self.buffer_list = BufferList
        self.modes = [
            'in_front_of',
            'on_call',
            'equals_with'
        ]
        self.string_abs = [
            "str",
            "string",
            "strings"
        ]
        self.int_abs = [
            "int",
            "integer",
            "number"
        ]
        self.dict_abs = [
            "dict",
            "dictionary",
            "json"
        ]
        self.bool_abs = [
            "bool",
            "boolean",
            "true-false"
        ]
    
    def getDictArgv(self):
        return BufferList(sys.argv).parse()
    
    def isArray(self, array: str):
        try:
            return {"is_array": True, "array": json.loads(array)}
        except:return {"is_array": False}

    def isBoolean(self, boolean: str):
        try:
            if boolean.startswith("t"):
                return {"is_boolean": True, "boolean": bool("T"+boolean[1:])}
            elif boolean.startswith("f"):
                return {"is_boolean": True, "boolean": bool("F"+boolean[1:])}
            else:return {"is_boolean": True, "boolean": bool(boolean)}
        except:return {"is_boolean": False}
    
    def addFlag(self, *flags, mode: modes = "in_front_of", obj_type: str = "str"):
        def decorator(func):
            self.handlers.append({func: {"flags": list(set(flags)), "mode": mode, "type": obj_type.lower()}})
            return func
        return decorator
    
    def on(self, *flags, mode: modes = "in_front_of", obj_type: str = "str"):
        def decorator(func):
            self.handlers.append({func: {"flags": list(set(flags)), "mode": mode, "type": obj_type.lower()}})
            return func
        return decorator
    
    def setFilter(self, flags_list: list, err_message: str, _exit: bool = True):
        """
        Check The all arguments and detect the mistakes\n

        Use 'B@ARGV' key word in your err_message to see invalid argument:\n

        buffer.setFilter(\n
            flags_list=[ '-h', '--help' ],\n
            err_message="Invalid Key: B@ARGV",
            _exit=True
            )

        Parameters:
            - **flags_list** (list): The flags used in the script.
            - **err_message** (str): Message printed if an invalid argument is detected.
            - **_exit** (bool): If True, the program will terminate upon detecting an invalid argument.
        """

        flags = list(set(flags_list))
        argvs = sys.argv

        for argv in argvs:
            if argv.startswith("-"):
                if not argv in flags:
                    print(err_message.replace("B@ARGV", argv))

                    if _exit:
                        exit(1)

    def trust(self):
        for handler in self.handlers:
            func = list(handler.keys())[0]
            flags = handler[func]['flags']
            mode = handler[func]['mode']
            type = handler[func]['type']

            argv = self.buffer_list(sys.argv).parse()
            arg_key = list(argv.keys())
            arg_val = list(argv.values())

            if mode == "in_front_of":

                for flag in flags:

                    setattr(self.last_things, flag.replace("-", ""), "NONECALL")

                    if flag in arg_val:
                        arg_index = arg_val.index(flag)
                        ifo_key = str(arg_index+2)
                        cleared_key = argv[str(arg_index+1)].replace("-", "")

                        if ifo_key in arg_key:

                            if type in self.string_abs:
                                setattr(self.last_things, cleared_key, argv[ifo_key])
                                
                            elif type in self.int_abs:
                                if argv[ifo_key].isdigit():
                                    setattr(self.last_things, cleared_key, int(argv[ifo_key]))
                                else:setattr(self.last_things, cleared_key, argv[ifo_key])

                            elif type in self.dict_abs:
                                status = self.isArray(argv[ifo_key])

                                if status['is_array']:
                                    setattr(self.last_things, cleared_key, status['array'])
                                else:setattr(self.last_things, cleared_key, argv[ifo_key])
                                
                            elif type in self.bool_abs:
                                status = self.isBoolean(argv[ifo_key])

                                if status['is_boolean']:
                                    setattr(self.last_things, cleared_key, status['boolean'])
                                else:setattr(self.last_things, cleared_key, argv[ifo_key])
                        else:
                            setattr(self.last_things, cleared_key, "Null")

            elif mode == "on_call":
                for flag in flags:

                    setattr(self.last_things, flag.replace("-", ""), "NONECALL")

                    if flag in arg_val:
                        arg_index = arg_val.index(flag)
                        k = argv[str(arg_index+1)]
                        cleared_key = k.replace("-", "")

                        if k in arg_val:
                            setattr(self.last_things, cleared_key, True)

                        else:
                            setattr(self.last_things, cleared_key, False)

            elif mode == "equals_with":
                for flag in flags:
                    setattr(self.last_things, flag.replace("-", ""), "NONECALL")
                    for arg in sys.argv:
                        if arg.startswith(flag):
                            if "=" in arg:
                                splitted_data = arg.split("=")[-1]

                                if type in self.string_abs:
                                    setattr(self.last_things, flag.replace("-", ""), splitted_data)

                                elif type in self.int_abs:
                                    if splitted_data.isdigit():
                                        setattr(self.last_things, flag.replace("-", ""), int(splitted_data))
                                    else:
                                        setattr(self.last_things, flag.replace("-", ""), splitted_data)

                                elif type in self.dict_abs:
                                    status = self.isArray(splitted_data)
                                    
                                    if status['is_array']:
                                        setattr(self.last_things, flag.replace("-", ""), status['array'])
                                    else:setattr(self.last_things, flag.replace("-", ""), splitted_data)
                                
                                elif type in self.bool_abs:
                                    status = self.isBoolean(splitted_data)

                                    if status['is_boolean']:
                                        setattr(self.last_things, flag.replace("-", ""), status['boolean'])
                                    else:setattr(self.last_things, flag.replace("-", ""), splitted_data)
                                else:setattr(self.last_things, flag.replace("-", ""), splitted_data)
                            else:setattr(self.last_things, flag.replace("-", ""), "NONEEQUALS")
                        
            func(self.last_things)

def get_all_packages() -> list[str]:
    data = []
    installed_packages = pkg_resources.working_set
    package_list = sorted(["{}=={}=={}".format(i.key, i.version, i.location) for i in installed_packages])

    for package in package_list:
        data.append(package.replace("==", " "))

    return data

buffer = BufferConsole()
lis = Licenses()
console = Console()

@buffer.on("--packages", mode="on_call")
def onPackages(things: Things):
    if things.packages == True:
        console.print()
        table = Table(title="Packages", title_justify="center")

        table.add_column("Package Name", justify="left", style="bold yellow")
        table.add_column("Version", justify="center", style="bold green")
        table.add_column("Location", justify="center", style="bold cyan")

        for package in get_all_packages():
            splitted = package.split(" ")
            name = splitted[0]
            version = splitted[1]
            location = splitted[2]

            table.add_row(
                name,
                version,
                location
            )

        console.print(table)

@buffer.on("--fetch", mode="equals_with")
def onFetch(things: Things):
    if not things.fetch == "NONECALL":
        if not things.fetch == "NONEEQUALS":
            console.log("[bold green]Fetching Mode Activated", justify='center')
            console.print("[yellow]FFP [cyan]info[/cyan] ", end="")
            console.print(f" [bold white]Trying to Download", end="")
            console.print(f" '{things.fetch}'")
            console.print("[yellow]FFP[/yellow] [purple]warning[/purple][bold white] All Fetching Process will continue by PIP")
            os.system(f"pip install {things.fetch}")
        else:console.print("[yellow]FFP[/yellow] [red]error[/red][bold white] Cannot get the Module name")

@buffer.on("--config.name", mode="equals_with")
def onConfigName(things: Things):
    if not getattr(things, "config.name") == "NONECALL":
        if not getattr(things, "config.name") == "NONEEQUALS":
            console.print(f"[yellow]FFP [cyan]info[/cyan][bold white] Name selected as [green]'{getattr(things, 'config.name')}'[/green]")

@buffer.on("--config.year", mode="equals_with")
def onConfigYear(things: Things):
    if not getattr(things, "config.year") == "NONECALL":
        if not getattr(things, "config.year") == "NONEEQUALS":
            console.print(f"[yellow]FFP [cyan]info[/cyan][bold white] Year selected as [green]'{getattr(things, 'config.year')}'[/green]")

@buffer.on("--show", mode="on_call")
def onShow(things: Things):
    ...

@buffer.on("--which", mode="on_call")
def onWhich(things: Things):
    if not things.which == "NONECALL":
        if things.which == True:
            console.print(licenses_list)

@buffer.on("--license", mode="equals_with")
def onCreate(things: Things):
    if not things.license == "NONECALL":
        if not things.license == "NONEEQUALS":
            if not getattr(things, "config.name") in ("NONECALL", "NONEEQUALS"):
                if not getattr(things, "config.year") in ("NONECALL", "NONEEQUALS"):
                    if things.license in licenses_list:
                        abs_license = lis.create(things.license, name=getattr(things, "config.name"), year=getattr(things, "config.year"))
                        if things.show == True:
                            console.print()
                            console.print(abs_license)
                        else:setattr(things, "license_result", abs_license);setattr(things, "which_license", things.license);setattr(things, "license_author", getattr(things, "config.name"));setattr(things, "license_year", getattr(things, "config.year"))
                    else:console.print("[yellow]FFP[/yellow] [red]error[/red][bold white] Entered License is not Available, try [green]'--which'[/green] to see available licenses")
                else:console.print("[yellow]FFP[/yellow] [red]error[/red][bold white] Year was not set in Config")
            else:console.print("[yellow]FFP[/yellow] [red]error[/red][bold white] Name was not Set in Config")
        else:console.print("[yellow]FFP[/yellow] [red]error[/red][bold white] License was not Select")

@buffer.on("--pack", mode="on_call")
def onPacking(things: Things):
    if not things.pack == "NONECALL":
        if hasattr(things, "license_result"):
            note = {
                "author": things.license_author,
                "package_name": getWorker(),
                "package_version": "1.0.0",
                "lisence": things.which_license,
                "license_year": things.license_year,
                "license_wrote_in": time.ctime(time.time()),
                "lisence_text": things.license_result
            }

            with open("pack.json", "w") as file:
                file.write(json.dumps(note, indent=4, ensure_ascii=False))
                file.close()

            console.print(note)
        else:console.print("[yellow]FFP[/yellow] [red]error[/red][bold white] License information was not enter")

@buffer.on("--help", mode="on_call")
def onHelp(things: Things):
    if things.help == True:
        table = Table.grid(padding=1, pad_edge=True)
        console.print("FFP Table :butterfly:", justify="center")
        table.add_column("Argument", no_wrap=True, justify="left")
        table.add_column("Description", justify="center")

        table.add_row(
            "[bold white]--help [cyan]<NONE INPUT>[/cyan]",
            "[yellow]Show the Help Message"
        )

        table.add_row(
            "[bold white]--packages [cyan]<NONE INPUT>[/cyan]",
            "[yellow]Table to See All Installed Packages"
        )

        table.add_row(
            "[bold white]--which [cyan]<NONE INPUT>[/cyan]",
            "[yellow]List of Licenses"
        )

        table.add_row(
            "[bold white]--show [cyan]<NONE INPUT>[/cyan]",
            "[yellow]See the License Result"
        )
        
        table.add_row(
            "[bold white]--fetch [cyan]<PACKAGE NAME>[/cyan]",
            "[yellow]Install a Package\n"
            "[blue]Usage: [purple]--fetch[white]=[bold white]requests"
        )

        table.add_row(
            "[bold white]--license [cyan]<LICENSE(s)>[/cyan]",
            "[yellow]Select a License, use [green]'--which'[/green] to "
            "See All Licenses \n"
            "[blue]Usage: [purple]--license[white]=[bold white]MIT"
        )

        table.add_row(
            "[bold white]--config [cyan]<.ATTRIBUTES>[/cyan]",
            "[yellow]Attributes: [bold white][ [green]'name'[/green][white], [green]'year'[/green] [bold white]] \n"
            "[blue]Usage: [white]--config[white].[purple]name[white]=[bold white]Jack [red]|[blue] [white]--config[white].[purple]year[white]=[bold cyan]2024"
        )

        table.add_row(
            "[bold white]--pack [cyan]<NONE INPUT>[/cyan]",
            "[yellow]Create a file named [green]'pack.json'[/green]\n"
            "[blue]Keys: [bold white][ [green]'author'[white],\n"
            "[green]'package_name'[white], [green]'package_version'[white],\n"
            "[green]'license'[white], [green]'license_year'[white],\n"
            "[green]'license_wrote_in'[white], [green]'license_text'[white] [bold white]]"
        )

        console.print(table)

buffer.setFilter(
    [
        "--help",
        "--packages", "--which",
        "--show", "--fetch",
        "--license", "--pack",
        "--config.name", "--config.year"
    ],
    "Invalid Argument: B@ARGV\ntry `--help` to see usage"
)

buffer.trust()