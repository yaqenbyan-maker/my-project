import tkinter as tk
from tkinter import ttk
import random

# إعداد النافذة
root = tk.Tk()
root.title("مخطط المجمع المعماري")
root.geometry("1200x750")
root.configure(bg="#e9e9e9")

# العنوان
title = tk.Label(
    root,
    text="المخطط الهندسي للمجمع",
    font=("Arial", 22, "bold"),
    bg="#e9e9e9",
    fg="#1e293b"
)
title.pack(pady=10)

# الإطار الرئيسي
main_frame = tk.Frame(root, bg="#e9e9e9")
main_frame.pack(fill="both", expand=True, padx=15, pady=5)

# لوحة الرسم
canvas = tk.Canvas(
    main_frame,
    bg="#86a66c",
    highlightthickness=2,
    highlightbackground="#555555"
)
canvas.pack(side="left", fill="both", expand=True)

# لوحة التحكم
control_frame = tk.Frame(main_frame, width=220, bg="#ffffff")
control_frame.pack(side="right", fill="y", padx=(12, 0))
control_frame.pack_propagate(False)

tk.Label(
    control_frame,
    text="التحكم",
    font=("Arial", 17, "bold"),
    bg="white",
    fg="#1e293b"
).pack(pady=15)


def draw_road(x1, y1, x2, y2, width=45):
    canvas.create_line(
        x1, y1, x2, y2,
        fill="#30343b",
        width=width
    )


def draw_parking(x, y, width, height):
    canvas.create_rectangle(
        x, y, x + width, y + height,
        fill="#24282d",
        outline="#111111"
    )

    # خطوط المواقف
    for px in range(x + 15, x + width - 5, 25):
        canvas.create_line(
            px, y + 5, px, y + height - 5,
            fill="white",
            width=1
        )


def draw_tree(x, y):
    canvas.create_oval(
        x - 10, y - 10, x + 10, y + 10,
        fill="#176b3a",
        outline="#0f4828"
    )
    canvas.create_rectangle(
        x - 2, y + 5, x + 2, y + 16,
        fill="#654321",
        outline=""
    )


def draw_building(x, y, width, height, label):
    # ظل المبنى
    canvas.create_rectangle(
        x + 7, y + 7,
        x + width + 7, y + height + 7,
        fill="#52616b",
        outline=""
    )

    # جسم المبنى
    canvas.create_rectangle(
        x, y, x + width, y + height,
        fill="#edf2f7",
        outline="#34495e",
        width=2
    )

    # السطح
    canvas.create_rectangle(
        x + 8, y + 8,
        x + width - 8, y + 23,
        fill="#b8c5d1",
        outline="#718096"
    )

    # الواجهات والنوافذ
    spacing = 24
    for wx in range(x + 15, x + width - 10, spacing):
        canvas.create_rectangle(
            wx, y + 35,
            wx + 10, y + height - 12,
            fill="#537aa5",
            outline="#27445d"
        )

    # المدخل
    canvas.create_arc(
        x + width // 2 - 15,
        y + height - 45,
        x + width // 2 + 15,
        y + height - 10,
        start=0,
        extent=180,
        fill="#263746",
        outline="#18242d"
    )

    canvas.create_text(
        x + width // 2,
        y + height // 2,
        text=label,
        fill="#1e293b",
        font=("Arial", 9, "bold")
    )


def draw_plan():
    canvas.delete("all")

    # خلفية خضراء
    canvas.create_rectangle(
        0, 0,
        canvas.winfo_width(),
        canvas.winfo_height(),
        fill="#87a96b",
        outline=""
    )

    # الطرق الرئيسية
    draw_road(30, 130, 780, 130, 42)
    draw_road(40, 520, 780, 520, 42)
    draw_road(180, 20, 180, 610, 38)
    draw_road(610, 20, 610, 610, 38)

    # أرصفة الطرق
    canvas.create_line(
        30, 108, 780, 108,
        fill="#d7a7a9",
        width=5
    )
    canvas.create_line(
        30, 152, 780, 152,
        fill="#d7a7a9",
        width=5
    )

    canvas.create_line(
        158, 20, 158, 610,
        fill="#d7a7a9",
        width=5
    )
    canvas.create_line(
        202, 20, 202, 610,
        fill="#d7a7a9",
        width=5
    )

    # المباني
    buildings = [
        (45, 35, 115, 75, "A1"),
        (235, 35, 130, 75, "A2"),
        (405, 35, 140, 75, "A3"),
        (650, 35, 110, 75, "A4"),

        (45, 190, 115, 85, "B1"),
        (235, 190, 140, 85, "B2"),
        (420, 190, 140, 85, "B3"),
        (655, 190, 105, 85, "B4"),

        (40, 350, 125, 85, "C1"),
        (235, 350, 145, 85, "C2"),
        (425, 350, 130, 85, "C3"),
        (655, 350, 105, 85, "C4"),

        (235, 555, 145, 65, "D1"),
        (425, 555, 130, 65, "D2"),
    ]

    for building in buildings:
        draw_building(*building)

    # مواقف السيارات
    draw_parking(270, 155, 130, 25)
    draw_parking(430, 155, 125, 25)
    draw_parking(270, 470, 130, 25)
    draw_parking(430, 470, 125, 25)

    # سيارات صغيرة
    for _ in range(25):
        x = random.randint(60, 735)
        y = random.choice([
            random.randint(108, 150),
            random.randint(505, 535)
        ])

        canvas.create_rectangle(
            x, y, x + 14, y + 7,
            fill=random.choice(
                ["#e74c3c", "#f1c40f", "#3498db", "#ecf0f1"]
            ),
            outline="#111111"
        )

    # أشجار
    for _ in range(45):
        x = random.randint(15, 790)
        y = random.randint(15, 620)

        # عدم وضع الأشجار داخل بعض المناطق المركزية
        if not (150 < x < 220 or 175 < y < 270):
            draw_tree(x, y)


def add_building():
    x = random.randint(250, 650)
    y = random.randint(230, 430)
    draw_building(x, y, 120, 70, "جديد")


def clear_plan():
    canvas.delete("all")
    canvas.configure(bg="#87a96b")


def show_info():
    info = tk.Toplevel(root)
    info.title("معلومات المشروع")
    info.geometry("350x220")
    info.resizable(False, False)

    tk.Label(
        info,
        text="معلومات المجمع",
        font=("Arial", 18, "bold")
    ).pack(pady=15)

    tk.Label(
        info,
        text=(
            "عدد المباني: 14\n"
            "المواقف: متعددة\n"
            "المساحات الخضراء: متوفرة\n"
            "النموذج: تصميم تجريبي"
        ),
        font=("Arial", 13),
        justify="center"
    ).pack(pady=10)


# أزرار التحكم
ttk.Button(
    control_frame,
    text="عرض المخطط",
    command=draw_plan
).pack(fill="x", padx=20, pady=8)

ttk.Button(
    control_frame,
    text="إضافة مبنى",
    command=add_building
).pack(fill="x", padx=20, pady=8)

ttk.Button(
    control_frame,
    text="مسح المخطط",
    command=clear_plan
).pack(fill="x", padx=20, pady=8)

ttk.Button(
    control_frame,
    text="معلومات",
    command=show_info
).pack(fill="x", padx=20, pady=8)

tk.Label(
    control_frame,
    text="الألوان",
    font=("Arial", 13, "bold"),
    bg="white"
).pack(pady=(35, 8))

for color, name in [
    ("#edf2f7", "المباني"),
    ("#30343b", "الطرق"),
    ("#87a96b", "المساحات الخضراء"),
    ("#d7a7a9", "الأرصفة")
]:
    row = tk.Frame(control_frame, bg="white")
    row.pack(fill="x", padx=25, pady=3)

    tk.Label(
        row,
        width=3,
        bg=color,
        relief="solid"
    ).pack(side="left")

    tk.Label(
        row,
        text=name,
        bg="white",
        font=("Arial", 10)
    ).pack(side="left", padx=8)


# تشغيل الرسم بعد ظهور النافذة
root.after(300, draw_plan)
root.mainloop()