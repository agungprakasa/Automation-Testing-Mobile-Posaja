from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import time
import os
import datetime
import traceback
import requests

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "emulator-5554"
options.app_package = "com.posindonesia.cob"
options.app_activity = ".MainActivity"
options.no_reset = True

driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", options=options)
driver.remove_app("com.posindonesia.cob")
# driver.install_app("posajamobiledev.apk")
driver.install_app("D:/QA/apkPOS/posajamobiledev.apk")

driver.activate_app("com.posindonesia.cob")

# === KONFIG TELEGRAM ===
BOT_TOKEN = '7700320759:AAHC0ufJWzBsteFFfyoXg27cO7cCfZkcR00'   # Ganti token kamu
CHAT_ID = '-4800804566'               # Ganti chat ID kamu

# === FOLDER ===
os.makedirs("logs", exist_ok=True)
os.makedirs("screenshots", exist_ok=True)

def kirim_file_ke_telegram(filepath, caption):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendDocument'
    with open(filepath, 'rb') as f:
        files = {'document': f}
        data = {'chat_id': CHAT_ID, 'caption': caption}
        requests.post(url, files=files, data=data)
    print(f"✅ File dikirim ke Telegram: {filepath}")

def handle_error(driver, err):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # === Screenshot ===
    screenshot_path = f"screenshots/error_{timestamp}.png"
    driver.save_screenshot(screenshot_path)
    print(f"[!] Screenshot disimpan: {screenshot_path}")

    # === Simpan Log Error ===
    log_path = f"logs/error_{timestamp}.txt"
    with open(log_path, "w", encoding="utf-8") as log_file:
        log_file.write("Traceback:\n")
        log_file.write(traceback.format_exc())
        log_file.write("\n\nURL saat error:\n")
        try:
            log_file.write(driver.current_url)
        except:
            log_file.write("Gagal mengambil URL")

    print(f"[!] Log disimpan: {log_path}")

    # === Kirim ke Telegram ===
    kirim_file_ke_telegram(screenshot_path, "📸 Screenshot error Selenium")
    kirim_file_ke_telegram(log_path, "📝 Log error Selenium")

try:
    wait = WebDriverWait(driver, 10)
    
    # permission_button = WebDriverWait(driver, 50).until(
    #     EC.element_to_be_clickable((By.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button"))
    # )
    # permission_button.click()
    
    time. sleep(10)
    klik_next = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Next']"))
    )
    klik_next.click()
    klik_done = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Done']"))
    )
    klik_done.click()
    
    klik_register = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='REGISTRASI SEKARANG']"))
    )
    klik_register.click()
    

    time.sleep(5)
    # driver.save_screenshot("login_error.png")
    pulihkan_akun = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='PULIHKAN AKUN']"))
    )
    pulihkan_akun.click()

    time.sleep(10)
    # print("Username atau password salah")
    # # Case 2
    nomor = driver.find_element(By.XPATH, "//android.widget.EditText[@text='Masukkan nomor ponsel']")
    nomor.send_keys("08123")
    nomor = driver.find_element(By.XPATH, "//android.widget.EditText[@text='Masukkan email']")
    nomor.send_keys("myposApp@email.com")

    

    # password_input.clear()
    # password_input.send_keys("AAaa123$")

    pulihkan = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Pulihkan']"))
    )
    pulihkan.click()

    time.sleep(10)
    # driver.save_screenshot("login_berhasil.png")


    print("Berhasil Pulihkan Akun")

    klik_reguler = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.ImageView"))
    )
    klik_reguler.click()
    
    pilihorder = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Pilih Order']"))
    )
    pilihorder.click()

    pickup = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='PICKUP']"))
    )
    pickup.click()

    aktif_cod = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup"))
    )
    aktif_cod.click()
    time.sleep(15)

    klik_penerima  = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]"))
    )
    klik_penerima.click()
    time.sleep(3)
    alamat_penerima = driver.find_element(By.XPATH, "//android.widget.EditText[@text='Masukkan kel / kec/ kota / kodepos']")
    alamat_penerima.send_keys("40115")
    time.sleep(5)

    klik_alamatpen  = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]"))
    )
    klik_alamatpen.click()
    time.sleep(5)

    detail_alamatpen = driver.find_element(By.XPATH, "//android.widget.EditText[@text='Contoh nomor jalan/blok dll']")
    detail_alamatpen.send_keys("jl gagak gang reuma")
    nama_penerima = driver.find_element(By.XPATH, "//android.widget.EditText[@text='Masukkan nama lengkap']")
    nama_penerima.send_keys("Martindes")
    no_penerima = driver.find_element(By.XPATH, "//android.widget.EditText[@text='Masukkan nomor handphone']")
    no_penerima.send_keys("088218320463")

    email_penerima = driver.find_element(By.XPATH, "//android.widget.EditText[@text='Masukkan alamat email']")
    email_penerima.send_keys("martin@gmail.com")

    # driver.execute_script("mobile: scroll", {
    #     "direction": "up"
    # })
    driver.find_element(
        by=By.ANDROID_UIAUTOMATOR,
        value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Simpan"))'
    )

    klik_simpan  = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Simpan']"))
    )
    klik_simpan.click()
    time.sleep(5)

    klik_berat  = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[1]"))
    )
    klik_berat.click()
    time.sleep(2)

    berat = driver.find_element(By.XPATH, "//android.widget.EditText[@text='Masukkan berat']")
    berat.send_keys("1000")
    close_b  = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup"))
    )
    close_b.click()
    time.sleep(2)
    
    klik_isikiriman  = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup[1]"))
    )
    klik_isikiriman.click()
    time.sleep(2)
    isi_kiriman = driver.find_element(By.XPATH, "//android.widget.EditText[@text='Contoh: baju / sepatu dll']")
    isi_kiriman.send_keys("Baju")
    close_i  = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup"))
    )
    close_i.click()
    time.sleep(2)

    klik_volumetrik  = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup[1]"))
    )
    klik_volumetrik.click()
    time.sleep(2)
    p = driver.find_element(By.XPATH, "//android.widget.EditText[@text='Panjang']")
    p.send_keys("5")
    l = driver.find_element(By.XPATH, "//android.widget.EditText[@text='Lebar']")
    l.send_keys("5")
    t = driver.find_element(By.XPATH, "//android.widget.EditText[@text='Tinggi']")
    t.send_keys("5")

    klik_simpanplt  = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Simpan']"))
    )
    klik_simpanplt.click()
    time.sleep(5)

    nilai_barang  = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Nilai barang']"))
    )
    nilai_barang.click()

    input_nilai = driver.find_element(By.XPATH, "//android.widget.EditText[@text='Masukkan nilai barang']")
    input_nilai.send_keys("100000")
    time.sleep(2)
    close_inputnilai  = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup"))
    )
    close_inputnilai.click()
    time.sleep(2)
    klik_cod  = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup"))
    )
    klik_cod.click()
    time.sleep(2)
    driver.find_element(
        by=By.ANDROID_UIAUTOMATOR,
        value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("CEK TARIF"))'
    )

    klik_cektarif  = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='CEK TARIF']"))
    )
    klik_cektarif.click()
    time.sleep(5)
    print("Berhasil Cek tarif")

    
    driver.find_element(
        by=By.ANDROID_UIAUTOMATOR,
        value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("PILIH"))'
    )
    klik_pilih  = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='PILIH']"))
    )
    klik_pilih.click()
    time.sleep(5)
    klik_permission  = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']"))
    )
    klik_permission.click()
    time.sleep(5)
    klik_selanjutnya  = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='SELANJUTNYA']"))
    )
    klik_selanjutnya.click()
    time.sleep(3)
    
    klik_notifno  = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@resource-id='android:id/button2']"))
    )
    klik_notifno.click()
    time.sleep(3)
    klik_centangcod  = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup"))
    )
    klik_centangcod.click()
    time.sleep(3)

    driver.find_element(
        by=By.ANDROID_UIAUTOMATOR,
        value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("ORDER"))'
    )
    klik_ORDER  = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='ORDER']"))
    )
    klik_ORDER.click()
    time.sleep(10)
    print("Berhasil Order COD PICKUP POS REGULER")
    driver.save_screenshot("berhasilorderpickupcod.png")
    
except Exception as e:
    print("[!] Terjadi ERROR:")
    traceback.print_exc()
    handle_error(driver, e)

    
finally:
    driver.quit()

