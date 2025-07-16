# Hotel Management

## Giới thiệu

**Hotel Management** là một hệ thống quản lý khách sạn, cho phép khách hàng đặt phòng trực tuyến và giúp nhân viên/quản lý dễ dàng theo dõi, xử lý các nghiệp vụ liên quan đến phòng, khách hàng, thanh toán, và báo cáo doanh thu. Hệ thống hướng đến việc tự động hóa và tối ưu hóa quy trình vận hành khách sạn.

## Tính năng chính

- **Đặt phòng trực tuyến:**  
  Khách hàng có thể chọn loại phòng, nhập thông tin cá nhân, số lượng người ở, ngày nhận và trả phòng, và gửi yêu cầu đặt phòng qua giao diện web.

- **Quản lý phòng:**  
  Xem danh sách phòng, thông tin chi tiết từng phòng, loại phòng, giá cả, hình ảnh, mô tả, diện tích, loại giường, tầm nhìn,...

- **Lập phiếu thuê phòng:**  
  Nhân viên có thể lập phiếu thuê phòng cho khách, tìm kiếm thông tin khách hàng và thông tin đặt phòng.

- **Thanh toán & xuất hóa đơn:**  
  Hỗ trợ thanh toán, tính tổng tiền dựa trên loại phòng và số ngày lưu trú, xuất phiếu hóa đơn.

- **Báo cáo doanh thu:**  
  Quản trị viên có thể xem báo cáo doanh thu, thống kê hoạt động kinh doanh.

- **Quản lý người dùng và phân quyền:**  
  Hỗ trợ nhiều vai trò như khách hàng, nhân viên, quản trị viên; mỗi vai trò có quyền hạn riêng biệt.

## Công nghệ sử dụng

- **Backend:** Python (Flask), SQLAlchemy ORM, SQLite/MySQL
- **Frontend:** HTML, CSS, JavaScript (Jinja2 Template)
- **Authentication:** Flask-Login
- **Quản trị:** Flask-Admin

## Khởi động dự án

### 1. Cài đặt môi trường

```bash
git clone https://github.com/Xhoangduy/Hotel_Management.git
cd Hotel_Management
python -m venv venv
source venv/bin/activate  # hoặc venv\Scripts\activate trên Windows
pip install -r requirements.txt
```

### 2. Khởi tạo CSDL

- Cấu hình thông tin CSDL trong `app/__init__.py` hoặc `.env`
- Tạo database:
```bash
python app/models.py
```

### 3. Chạy ứng dụng

```bash
python app/index.py
```
Truy cập tại: [http://localhost:5000](http://localhost:5000)

## Cấu trúc thư mục

```
Hotel_Management/
├── app/
│   ├── __init__.py
│   ├── index.py        # Xử lý các route chính
│   ├── admin.py        # Quản trị, báo cáo, phân quyền
│   ├── models.py       # Định nghĩa các bảng, ORM
│   ├── dao.py          # Các hàm truy vấn dữ liệu
│   ├── templates/      # Giao diện HTML
│   ├── static/         # File tĩnh (ảnh, css, js)
│   └── ...
├── requirements.txt
└── README.md
```

## Đóng góp

Vui lòng tạo issue mới để báo lỗi hoặc đề xuất tính năng. PR (Pull Request) luôn được hoan nghênh!

## License

Dự án chưa công bố license cụ thể.

---

> © 2025 Xhoangduy. Mọi thông tin chi tiết vui lòng liên hệ qua GitHub: [Xhoangduy](https://github.com/Xhoangduy)
