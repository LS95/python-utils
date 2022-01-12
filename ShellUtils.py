# coding=utf-8
'''
获取cmd命令行输出
ref：https://github.com/lijiejie/log4j2_vul_local_scanner
'''
import sys
import subprocess

if sys.version_info < (2, 7):
    from subprocess import PIPE, Popen  # python2.6 has no check_output


def get_cmd_out(cmd):
    try:
        if sys.version_info < (2, 7):
            proc = Popen(cmd.split(), stdout=PIPE)  # python2.6
            return proc.communicate()[0].strip()
        else:
            out = subprocess.check_output(cmd, shell=True).strip()
            return out.decode()
    except Exception as e:
        return ""


def test():
    cmdLists = ["ls -al", "whoami", "ifconfig", "notAcommand"]
    for eachCmd in cmdLists:
        print(eachCmd, " >>>>  ", get_cmd_out(eachCmd))


if __name__ == '__main__':
    test()
