import trans_img
import new_getwav
import send_wav
import time
import test_noise
import generate_wav
import recall_wav


flag = input('Who are you?(0: Sender / 1: Receiver / 2: Simulation / 3: Other function): ')

if flag == '0':
    file_path = input('The address of the image file: ')
    out_path = input('The name of wav file: ')
    trans_img.img2wav(file_path, out_path)
    print('Processing completed!')
    time.sleep(2)
    print('Sending...')
    send_wav.do_work(out_path)
    print('Sending completed!')

elif flag == '1':
    file_name = input('The address we want to save the wav file: ')
    new_getwav.listen(True, file_name)
    time.sleep(2)
    out_name = input('The address of output file: ')
    trans_img.draw_figure(file_name, out_name)
    print('Completed!')

elif flag == '2':
    img_path = input('The PNG file: ')
    wav_path = input('INFO wav file: ')
    trans_img.img2wav(img_path, wav_path)
    time.sleep(2)
    noise_out = input("Add the noise(Address of output): ")
    test_noise.generate_wav(wav_path, "noise.wav", noise_out)
    time.sleep(2)
    print("Mix the wav")
    back_path = input('The background file: ')
    muli_path = input('The mixture file: ')
    generate_wav.generate_wav_s(back_path, noise_out, muli_path)
    time.sleep(2)
    print('Now recover the img')
    img_final = input('The output img file: ')
    recall_wav.return_wav_s(muli_path, back_path, 're.wav')
    time.sleep(2)
    trans_img.draw_figure('re.wav', img_final)
    print("Finished! ")

elif flag == '3':
    vis = input("Generate (0) or Recover (1): ")
    if vis == '0':
        img_path = input('The PNG file: ')
        wav_path = input('INFO wav file: ')
        trans_img.img2wav(img_path, wav_path)
        time.sleep(2)
        back_path = input('The background file: ')
        out_wav = input('The output file: ')
        generate_wav.generate_wav(wav_path, back_path, out_wav)
    elif vis == '1':
        origin_wav = input('The original wav: ')
        back_wav = input('The background wav: ')
        recall_wav.return_wav(origin_wav, back_wav, "im.wav")
        time.sleep(2)
        out_img = input('The img file: ')
        trans_img.draw_figure("im.wav", out_img)
        print("Completed! ")


