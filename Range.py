down = 0
up = 100
for i in range(1,10):
    guessed_age = int((up + down)/ 2)
    answer = input('apakah kamu berumur ' + str(guessed_age) + " tahun?")
    if answer == 'benar' :
        print("bagus")
        break
    elif answer == 'kurang' :
        up = guessed_age
    elif answer == 'tambah':
        down = guessed_age
    else:
        print('jawaban salah')