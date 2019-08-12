import os, sys

print ("\033[1;34mSilahkan Masukkan ID & Password Anda")

print ("\033[1;35matau silahkan Hubungi 081316577616 ")
print ("\033[1;33mJgn Ngasal Cok ntr salah ")
ID = 'TheSploit'      

password = 'Sploit1109'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("ID : ")

	if uname == ID:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\034[1;32mSuksess Login To My-Tools..", 

			sys.exit()



		else:

			print "\033[1;32mMaaf Password Anda Salah Silahkeun Coba Lagi... [?]\033[00m"

			print "Silahkan log-in kembali untuk Masuk ke My-Tools...!!\n"

			restart()



	else:

		print "\033[1;32mMaaf  ID Anda salah Silahkeun Check Kembali Untuk Masuk... [?]\033[00m"

		print "Silahkan log-in kembali untuk Login ke My-Tools...!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()
