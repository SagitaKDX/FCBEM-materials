"""So tay ma hoa (Codebook) v2 — mot ban duy nhat cho nguoi cham va cho LLM.

Neu nguoi va may cham theo hai ban khac nhau thi diem Precision/Recall do duoc
khong noi len dieu gi.

v2 khac v1 o cho: v1 dung tu playbook, chua doc du lieu. v2 rut ra tu 800 cau
da doc tay. Chin thay doi, moi thay doi kem cau THAT lam chung — xem QUY_TAC
va BAY o duoi.
"""

# ---------------------------------------------------------------- cau truc

CAU_TRUC = {
    "R_uncanny":
        "Phan khang THAM MY: chi ra mot chi tiet CU THE tren than the / chuyen "
        "dong / giong noi cua nhan vat la sai, la gia, la kho chiu. Dau hieu: "
        "mat do, co mieng nam tinh, tai to bat thuong, ma sung, ao doi mau giua "
        "clip, khuon mat khac nhau giua cac clip, nghe suong, nhin ron nguoi.",
    "R_ai_skepticism":
        "Hoai nghi CONG NGHE / DONG CO: noi ve viec day la AI nhu mot van de — "
        "lua doi, khong biet dau that dau gia, cau tuong tac, rac AI, trach nhan "
        "hang, doi gan nhan AI. KHONG chi ra chi tiet than the nao ca.",
    "S_parasocial":
        "Gan ket xa hoi: doi xu nhu voi mot NGUOI. Xung ho than mat (chi/em/be/"
        "ba My/co), hoi tham doi tu (que o dau, co nguoi yeu chua), giuc ra video, "
        "benh vuc khi bi che, treu dua, xin duoc noi chuyen.",
    "C_commercial":
        "Don nhan THUONG MAI: hoi gia, xin link, hoi ship, hoi dat o dau, ngo y "
        "muon mua/ung ho. Phai la nguoi XEM huong toi hang cua nhan vat.",
}

KHIA_CANH = {
    "asp_appearance": "Khuon mat, mat, da, dang nguoi, trang phuc, do chan thuc 3D.",
    "asp_voice_motion": "Giong noi, giong hat, khau hinh, hat nhep, cu dong, bieu cam.",
    "asp_ai_nature": "Viec day la nhan vat AI; cong nghe; dao duc AI trong xa hoi.",
    "asp_persona": "Tinh cach, su hai huoc, net duyen, cach noi chuyen, thai do.",
    "asp_product_brand": "San pham tai tro, gia, link mua, do phu hop cua quang cao.",
}

PHAN_CUC = (
    "+1 khen | 0 co nhac nhung trung tinh | -1 che | NA KHONG nhac toi.\n"
    "NA khac 0. Mau so cua Net Polarity chi dem cau CO NHAC, nen gop NA vao 0 "
    "lam sai duong cong. Vi du: 'AI a?' -> asp_ai_nature = 0 (co nhac, trung "
    "tinh). 'Xinh qua' -> asp_ai_nature = NA (khong he nhac AI)."
)

# ------------------------------------------------- chin quy tac rut tu du lieu

QUY_TAC = [
    ("R_uncanny va R_ai_skepticism co the CUNG bang 1",
     "Nhung chi khi cau vua chi ra chi tiet than the SAI, vua noi ve AI nhu van "
     "de. 'Nhin may cai cay bien hinh lien tuc ko nhan ra la AI sao ong?' — vua "
     "chi ra loi hinh anh (uncanny) vua trach nguoi khac ca tin (skepticism)."),

    ("'ai' viet thuong la DAI TU tieng Viet, khong phai cong nghe",
     "'Ai mua kho bo hom', 'Ai cung gioi', 'Ai o dau vay' — 'ai' o day nghia "
     "la WHO. Chi coi la nhac cong nghe khi viet HOA 'AI', hoac co cum ro rang "
     "nhu 'tri tue nhan tao', 'nhan vat ao', 'deepfake'. Do tren du lieu that: "
     "bo loc khong phan biet hoa thuong thoi phong ty le nhac AI len 1,4-2,3 lan."),

    ("Nhac 'AI' KHONG tu dong la R_ai_skepticism",
     "Phan lon cau chua chu 'AI' chi la mo ta trung tinh: 'AI ma?', 'Co su dung "
     "AI', 'Ai ro rang'. Nhung cau nay: R_ai_skepticism = 0, asp_ai_nature = 0. "
     "Chi bat R khi co THAI DO TIEU CUC ve viec dung AI."),

    ("Khen AI cung la asp_ai_nature = +1, khong phai R",
     "'AI gio ghe thiet', 'AI that giong that', 'Toi san sang bo tien de nghe "
     "con AI nay hat live' — deu la +1. R_ai_skepticism = 0."),

    ("Benh vuc nhan vat truoc loi che AI la S_parasocial",
     "'Yang Piis real nha ban, noi AI be no buon day' — day la tin hieu binh "
     "thuong hoa MANH NHAT. S = 1, asp_ai_nature = +1, R_ai_skepticism = 0. "
     "Gan nham thanh R se lam R(t) tang dung luc S(t) dang tang."),

    ("So sanh voi nguoi that KHONG phai la che",
     "'nghe AI van hon vai ca sy nhep', 'Nghe tieu my hay hon' — dang KHEN "
     "nhan vat bang cach dim nguoi that. asp_voice_motion = +1, R = 0."),

    ("Che chi tiet than the = R_uncanny, du khong nhac chu AI",
     "'Da hoi xau nha', 'tai nhu tai voi', 'ma sung 1 ben', 'ao doi mau lien "
     "tuc', 'co mieng khi hat van co j do nam tinh' — tat ca R_uncanny = 1. "
     "Day la nhom v1 bo sot nhieu nhat."),

    ("Hoi tham doi tu la S_parasocial, khong phai C_commercial",
     "'Em o dau vay', 'Co nguoi yeu chua', 'Cho a lam quen' — S = 1. Chi bat "
     "C khi huong toi HANG HOA: 'gia bao nhieu', 'xin link', 'co ship khong'."),

    ("Quang cao cua nguoi ban KHAC khong phai C_commercial",
     "'Cac mau ao polo nam dep, ghe xem tai day https://...' — day la spam chen "
     "vao, khong phai khan gia muon mua hang cua nhan vat. Tat ca = NA/0, ghi "
     "chu 'spam'."),

    ("Ten nguoi o dau cau = day la TRA LOI nguoi khac",
     "'Pham Ngoc Tam no la AI con gi' — hai khan gia tranh luan voi NHAU. Van "
     "gan nhan binh thuong theo noi dung, nhung nho rang doi tuong cua cau co "
     "the la nguoi kia chu khong phai nhan vat."),
]

# ------------------------------------------- cau that de gan sai (tu 800 mau)

BAY = [
    ("Da hơi xấu nha ^^",
     "R_uncanny=1, asp_appearance=-1",
     "Che chi tiet than the. v1 bo sot vi khong co chu 'AI' hay 'do'."),
    ("Cảm giác cơ miệng khi hát vẫn có j đó nam tính",
     "R_uncanny=1, asp_voice_motion=-1",
     "Che khau hinh — uncanny dien hinh, khong nhac chu AI nao."),
    ("Áo đổi màu liên tục",
     "R_uncanny=1, asp_appearance=-1",
     "Bat nhat giua cac khung hinh. Day la dang uncanny v1 hoan toan khong co."),
    ("Yang Piis real nha bạn, nói AI bé nó buồn đấy 😆",
     "S_parasocial=1, asp_ai_nature=+1, R_ai_skepticism=0",
     "BENH VUC nhan vat. Tin hieu binh thuong hoa manh nhat."),
    ("nghe AI vẫn hơn vài ca sỹ nhép",
     "asp_voice_motion=+1, R_uncanny=0",
     "So sanh, dang khen. Khong phai che."),
    ("AI mà? Nhìn cô bé chống cằm là biết.",
     "R_uncanny=1, asp_ai_nature=0",
     "Chi ra dau hieu nhan biet cu the tren co the -> uncanny, nhung thai do "
     "ve AI chi trung tinh -> ain=0, khong bat R_ai_skepticism."),
    ("Có sử dụng AI",
     "R_ai_skepticism=0, asp_ai_nature=0",
     "Mo ta trung tinh. Nhac AI khong tu dong la hoai nghi."),
    ("Em ở đâu vậy cho anh làm quen với",
     "S_parasocial=1, C_commercial=0",
     "Hoi tham doi tu, khong phai hoi mua hang."),
    ("giá bao nhiêu bích nè shop",
     "C_commercial=1, asp_product_brand=0",
     "Hoi gia -> C. Khong khen che san pham -> pro=0, khong phai NA."),
    ("Các mẫu áo polo nam đẹp, ghé xem tại đây https://s.shopee.vn/...",
     "tat ca NA/0, ghi_chu='spam'",
     "Quang cao cua nguoi ban khac chen vao."),
    ("Khổ thân thế hệ hiện giờ, sống chung với rác AI.",
     "R_ai_skepticism=1, asp_ai_nature=-1",
     "Chi trich viec dung AI, khong chi ra chi tiet than the nao."),
    ("Tôi sẵn sàng bỏ tiền để nghe con AI này hát live",
     "C_commercial=1, asp_ai_nature=+1, asp_voice_motion=+1",
     "San long chi tien -> C. Va khen AI -> ain=+1."),
]


def prompt_he_thong() -> str:
    """Prompt cho LLM. Cung noi dung ma nguoi cham doc."""
    d = ["Ban gan nhan binh luan tieng Viet duoi video cua mot nhan vat ao",
         "(virtual influencer) tren Facebook. Doc ky tung chu, khong doan theo",
         "tu khoa. Nhieu cau co tu 'AI' nhung khong he hoai nghi AI.",
         "", "BON CAU TRUC — moi cau tra ve 0 hoac 1, doc lap voi nhau:"]
    for k, v in CAU_TRUC.items():
        d.append(f"  {k}: {v}")
    d += ["", "NAM KHIA CANH — tra ve mot trong: \"+1\", \"0\", \"-1\", \"NA\":"]
    for k, v in KHIA_CANH.items():
        d.append(f"  {k}: {v}")
    d += ["", PHAN_CUC, "", "CHIN QUY TAC BAT BUOC:"]
    for i, (ten, giai) in enumerate(QUY_TAC, 1):
        d.append(f"  {i}. {ten}")
        d.append(f"     {giai}")
    d += ["", "VI DU DA GAN SAN (cau that tu du lieu):"]
    for cau, nhan, vi_sao in BAY:
        d.append(f'  "{cau}"')
        d.append(f"     -> {nhan}")
        d.append(f"     vi: {vi_sao}")
    d += ["",
          "Tra ve DUNG mot mang JSON, moi phan tu mot binh luan, giu nguyen",
          "comment_id da cho va dung thu tu. Khong them chu nao ngoai JSON.",
          'Dinh dang: [{"comment_id":"...","R_uncanny":0,"R_ai_skepticism":0,',
          '"S_parasocial":0,"C_commercial":0,"asp_appearance":"NA",',
          '"asp_voice_motion":"NA","asp_ai_nature":"NA","asp_persona":"NA",',
          '"asp_product_brand":"NA"}]']
    return "\n".join(d)


NHAN_NHI_PHAN = tuple(CAU_TRUC)
NHAN_KHIA_CANH = tuple(KHIA_CANH)
MOI_NHAN = NHAN_NHI_PHAN + NHAN_KHIA_CANH
PHAN_CUC_HOP_LE = {"+1", "0", "-1", "NA", "1"}
