
CCFLAGS = ['-I/usr/include/lua5.1', '-O2', '-ansi']
# 自己通过命令 sudo find / -name "*liblua*" 来查静态库.a文件在哪, 然后把路径填到下面
LIBPATH = ['/usr/lib/x86_64-linux-gnu']
LIBS = ['lua5.1', 'dl', 'm']
#prefix = '/mingw'
#build_dev=1
tolua_bin = 'tolua++5.1'
tolua_lib = 'tolua++5.1'
TOLUAPP = 'tolua++5.1'
