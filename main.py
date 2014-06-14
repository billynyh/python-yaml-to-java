import sys
import yaml
import datetime

T = "    "

class Converter:
    def __init__(self, pkg):
        self.pkg = pkg

    def out_package(self, I=""):
        print "/* AUTO GEN CODE, DONT MODIFY"
        print " * last compile: %s" % str(datetime.datetime.now())
        print " */"
        print "package %s;" % self.pkg
        
    def out_class(self, name, content, I=""):
        if not type(content) is dict:
            return

        if I == "": # top level
            print I + "public class {name} {{".format(name = name)
        else: 
            print I + "public static class {name} {{".format(name = name)

        for k,v in content.items():
            self.out_field(k, v, I + T)

        print I + "}"

    def out_field(self, name, content, I):
        t = type(content)
        if t is dict:
            self.out_class(name, content, I)
        elif t is int:
            self.out_int(name, content, I)
        elif t is float:
            self.out_float(name, content, I)
        elif t is str:
            self.out_string(name, content, I)
        elif t is bool:
            self.out_boolean(name, content, I)
            
    def out_int(self, name, content, I):
        print I + "public static final int {0} = {1};".format(name, content)
    
    def out_float(self, name, content, I):
        print I + "public static final float {0} = {1};".format(name, content)

    def out_string(self, name, content, I):
        content = content.replace("\"", "\\\"")
        print I + "public static final String {0} = \"{1}\";".format(name, content)

    def out_boolean(self, name, content, I):
        value = "true" if content else "false"
        print I + "public static final boolean {0} = {1};".format(name, value)
            





def main(inputPath, pkgName):
    f = open(inputPath)
    dataMap = yaml.safe_load(f)
    f.close()

    root = "AppBuildConfig"
    converter = Converter(pkgName)
    converter.out_package()
    converter.out_class(root, dataMap[root])

try:
    fname = sys.argv[1]
    main(fname, "io.github.billynyh")
except Exception as e:
    print e
