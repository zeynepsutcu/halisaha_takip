# -*- coding: utf-8 -*-
"""
Created on Fri May 31 22:27:05 2024

@author: Lenovo
"""
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QHeaderView
from widgets_kullanıcı import *
import subprocess 
#--------kütüphane----------------
#-------uygulama----------------------#
Uygulama=QApplication(sys.argv)
penkullanıcı_ekranı=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(penkullanıcı_ekranı)
penkullanıcı_ekranı.show()

#-----------veri tabanı oluştur-------#
import sqlite3
global curs
global conn 
conn=sqlite3.connect('veriler.db')
curs=conn.cursor()
conn.commit()
#-------------kaydet------------------#
def ekle ():
    
    _lneAdi = ui.lneAdi.text()
    _lnesoyadi = ui.lnesoyadi.text()
    _lnetakim_adi = ui.lnetakim_adi.text()
    _lnekarsi_takim_adi= ui.lnekarsi_takim_adi.text()
    _lnemail = ui.lnemail.text()
    _lnetelefonnumarasi=ui.lnetelefon.text()
    _cmbpozisyon = ui.cmbpozisyon.currentText()
    _lneil = ui.lneil.text()
    _lneilce = ui.lneilce.text()
    _lnetesis = ui.lnetesis.text()
    _lnesaat=ui.lnesaat.text()
    _cwtarih = ui.cwtarih.selectedDate().toString(QtCore.Qt.ISODate)
    
     
    try:
       curs.execute("INSERT INTO uyeler \
                  (adi, soyadi, takim_adi, karsi_takim_adi,mail,telefon_numarasi, pozisyon, il, ilçe, tesis, saat, tarih) \
                  VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", \
                 (_lneAdi, _lnesoyadi, _lnetakim_adi, _lnekarsi_takim_adi, _lnemail, _lnetelefonnumarasi, _cmbpozisyon, \
                 _lneil, _lneilce, _lnetesis, _lnesaat, _cwtarih))
       conn.commit()
       QMessageBox.information(penkullanıcı_ekranı, "Bilgi", "Kayıt başarıyla eklendi.")
    except sqlite3.Error as e:
       QMessageBox.critical(penkullanıcı_ekranı, "Hata", f"Veritabanına ekleme sırasında bir hata oluştu: {e}")
       
def listele():
    ui.tableWidget.clear() 
    ui.tableWidget.setHorizontalHeaderLabels(('id','adi', 'soyadi', 'takim_adi', 'karsi_takim_adi', 'mail', 'telefon_numarasi', 
                                                    'pozisyon', 'il', 'ilçe','tesis', 'saat', 'tarih'))
    ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    
    curs.execute("SELECT * FROM uyeler")
    for satirIndeks, satirVeri in enumerate(curs.fetchall()):
        for sutunIndeks, sutunVeri in enumerate(satirVeri):
            ui.tableWidget.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))

        
def güncelle():
    cevap = QMessageBox.question(penkullanıcı_ekranı, "KAYIT GÜNCELLE", "Kayıt Güncellemek İstediğinize Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)
    if cevap == QMessageBox.Yes:
        
        selected_row = ui.tableWidget.currentRow()
        _no = ui.tableWidget.item(selected_row, 0).text()
        _lneAdi = ui.lneAdi.text()
        _lnesoyadi = ui.lnesoyadi.text()
        _lnetakim_adi = ui.lnetakim_adi.text()
        _lnekarsi_takim_adi = ui.lnekarsi_takim_adi.text()
        _lnemail = ui.lnemail.text()
        _lnetelefonnumarasi = ui.lnetelefon.text()
        _cmbpozisyon = ui.cmbpozisyon.currentText()
        _lneil = ui.lneil.text()
        _lneilce = ui.lneilce.text()
        _lnetesis = ui.lnetesis.text()
        _lnesaat = ui.lnesaat.text()
        _cwtarih = ui.cwtarih.selectedDate().toString(QtCore.Qt.ISODate)
        
        new_ad, ok1 = QInputDialog.getText(penkullanıcı_ekranı, "Güncelle", "Ad:", QLineEdit.Normal, _lneAdi)
        if not ok1 or new_ad.strip() == "":
            return
        new_soyad, ok2 = QInputDialog.getText(penkullanıcı_ekranı, "Güncelle", "Soyad:", QLineEdit.Normal,_lnesoyadi)
        if not ok2 or new_soyad.strip() == "":
            return
        new_takimadi, ok3 = QInputDialog.getText(penkullanıcı_ekranı, "Güncelle", "Takım Adı:", QLineEdit.Normal,_lnetakim_adi)
        if not ok3 or new_takimadi.strip() == "":
            return

        new_karsitakimadi, ok4 = QInputDialog.getText(penkullanıcı_ekranı, "Güncelle", "Karşı Takım Adı:", QLineEdit.Normal,_lnekarsi_takim_adi)
        if not ok4 or new_karsitakimadi.strip() == "":
            return
        new_mail, ok5 = QInputDialog.getText(penkullanıcı_ekranı, "Güncelle", "Mail:", QLineEdit.Normal,_lnemail)
        if not ok5 or new_mail.strip() == "":
            return
        new_telefonnumarasi, ok6 = QInputDialog.getText(penkullanıcı_ekranı, "Güncelle", "Telefon Numarası:", QLineEdit.Normal, _lnetelefonnumarasi)
        if not ok6 or new_telefonnumarasi.strip() == "":
            return

        new_pozisyon, ok7 = QInputDialog.getText(penkullanıcı_ekranı, "Güncelle", "pozisyon:", QLineEdit.Normal,_cmbpozisyon)
        if not ok7 or new_pozisyon.strip() == "":
            return
        new_il, ok8 = QInputDialog.getText(penkullanıcı_ekranı, "Güncelle", "İl:", QLineEdit.Normal,_lneil)
        if not ok8 or new_il.strip() == "":
            return
        new_ilce, ok9 = QInputDialog.getText(penkullanıcı_ekranı, "Güncelle", "İlçe:", QLineEdit.Normal,_lneilce)
        if not ok9 or new_ilce.strip() == "":
            return
        new_tesis, ok10 = QInputDialog.getText(penkullanıcı_ekranı, "Güncelle", "Tesis:", QLineEdit.Normal,_lnetesis)
        if not ok10 or new_tesis.strip() == "":
            return
        new_saat, ok11 = QInputDialog.getText(penkullanıcı_ekranı, "Güncelle", "Saat:", QLineEdit.Normal,_lnesaat)
        if not ok11 or new_saat.strip() == "":
            return
        new_tarih, ok12 = QInputDialog.getText(penkullanıcı_ekranı, "Güncelle", "Tarih:", QLineEdit.Normal, _cwtarih)
        if not ok12 or new_tarih.strip() == "":
            return

        

        try:
            
            curs.execute("""
                UPDATE uyeler SET 
                    adi = ?, soyadi = ?, takim_adi = ?, karsi_takim_adi = ?, mail = ?, telefon_numarasi = ?, 
                    pozisyon = ?, il = ?, ilçe = ?, tesis = ?, saat = ?, tarih = ? 
                WHERE id = ?
            """, (new_ad, new_soyad, new_takimadi, new_karsitakimadi,new_mail,new_telefonnumarasi, new_pozisyon, new_il,new_ilce,
                  new_tesis, new_saat, new_tarih,_no)) 
            conn.commit()
            QMessageBox.information(penkullanıcı_ekranı, "Bilgi", "Kayıt başarıyla güncellendi.")
            listele()
        except sqlite3.Error as e:
            QMessageBox.critical(penkullanıcı_ekranı, "Hata", f"Veritabanı hatası: {e}")

            
#---------sil-------#
def SIL():
    cevap = QMessageBox.question(penkullanıcı_ekranı, "KAYIT SİL", "Kaydı silmek istediğinize emin misiniz?",\
                               QMessageBox.Yes | QMessageBox.No)
    if cevap == QMessageBox.Yes:
        try:
            secili = ui.tableWidget.selectedItems()
            if secili:
                silinecek = secili[0].text()  
                curs.execute("DELETE FROM uyeler WHERE id=?", (silinecek))
                conn.commit()
                listele()
                ui.statusbar.showMessage("KAYIT SİLME İŞLEMİ BAŞARIYLA GERÇEKLEŞTİ...", 10000)
            else:
                ui.statusbar.showMessage("Silinecek bir kayıt seçilmedi.", 10000)
        except sqlite3.Error as Hata:
            ui.statusbar.showMessage("Şöyle bir hata ile karşılaşıldı: " + str(Hata))
    else:
        ui.statusbar.showMessage("Silme işlemi iptal edildi....", 10000)
listele()         

ui.pushButton_5.clicked.connect(penkullanıcı_ekranı.close)
ui.btnkayit.clicked.connect(ekle)
ui.pushButton_4.clicked.connect(listele)
ui.pushButton_3.clicked.connect(güncelle)
ui.pushButton_2.clicked.connect(SIL)

sys.exit(Uygulama.exec_())     