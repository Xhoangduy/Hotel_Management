import hashlib
from flask import render_template, request, redirect
import dao
from app import app, login
from app.models import User, RoomForm, Bill
from flask_login import login_user, logout_user, current_user
from app import db
from datetime import date
from datetime import datetime
from flask import flash

@app.route('/')
def index():
    kw = request.args.get('kw')
    pricefrom = request.args.get('pricefrom')
    priceto = request.args.get('priceto')
    type_id = request.args.get('type_id')
    rooms = dao.load_rooms(kw=kw, type_id=type_id, pricefrom=pricefrom, priceto=priceto)


    return render_template('index.html', rooms=rooms)


@app.route('/room/<id>')
def room_detail(id):
    room = dao.get_room_by_id(id)
    return render_template('viewroom.html', room=room)


@app.route('/admin/login', methods=['post'])
def login_admin_process():
    username = request.form.get('username')
    password = request.form.get('password')

    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user=user)
    return redirect('/admin')


@app.route("/login/signup", methods=['post'])
def signup():
    username = request.form.get('username')
    password = request.form.get('password')
    name = request.form.get('name')
    address = request.form.get('address')
    phone = request.form.get('phone')
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())
    check = User.query.filter(User.name.contains(username))
    if username == check:
        pass
    else:
        c = User(username=username, password=password, name=name, address=address, phone=phone)
        db.session.add(c)
        db.session.commit()
    return redirect("/login")


@app.route("/login/signin", methods=['post'])
def signin():
    username = request.form.get('username')
    password = request.form.get('password')
    user = dao.auth_user(username, password)
    if user:
        login_user(user)
        return redirect("/")
    else:
        return redirect("/login")


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/logout")
def logout():
    if load_user:
        logout_user()
    return redirect('/')


@app.route('/booking', methods=['GET', 'POST'])
@app.route('/room/booking', methods=['GET', 'POST'])
def booking():
    typeroom = dao.load_typeroom()
    
    if request.method == 'POST':
        try:
            name = request.form.get('nameuser')
            check_in = request.form.get('check-in')
            check_out = request.form.get('check-out')
            count = request.form.get('count')
            typeroom = request.form.get('type-room')

            if all([name, check_in, check_out, count, typeroom]):
                check_in_date = datetime.strptime(check_in, '%Y-%m-%d').date()
                check_out_date = datetime.strptime(check_out, '%Y-%m-%d').date()
                
                roomform = RoomForm(
                    name=name,
                    check_in=check_in_date,
                    check_out=check_out_date,
                    count=int(count),
                    typeroom=typeroom
                )
                
                try:
                    db.session.add(roomform)
                    db.session.commit()
                    flash("Đặt phòng thành công!")
                    return redirect('/createform')
                except Exception as db_error:
                    db.session.rollback()
                    flash(f"Lỗi khi lưu vào CSDL: {str(db_error)}")
            else:
                flash("Vui lòng điền đầy đủ thông tin")
        except Exception as e:
            flash(f"Lỗi xử lý dữ liệu: {str(e)}")
        return redirect('/booking')

    return render_template('booking.html', typeroom=typeroom)


@app.route('/createform')
def create_form():


    return render_template('createForm.html',  roomform = dao.load_roomform())

@app.route('/createform/roomform/<id>')
def room_form(id):

    return render_template('roomform.html',  roomform = dao.get_roomform_by_id(id))
@app.route('/createform/<id>', methods =['GET', 'POST'])
def delete_form(id):

    if request.method == "GET":
        roomform = RoomForm.query.get(id)
        if roomform:
            db.session.delete(roomform)
            db.session.commit()
            return "Xóa dòng dữ liệu thành công!"
        else:
            return "Dòng dữ liệu không tồn tại!"
    else:
        return "Hủy xóa dòng dữ liệu!"

    return render_template('createform.html', roomform = roomform)

@app.route('/pay')
def pay():
    roomform = dao.load_roomform()
    return render_template('pay.html', roomform=roomform)
@app.route('/pay/<id>', methods =['GET', 'POST'])
def delete_bill(id):

    if request.method == "GET":
        roomform = RoomForm.query.get(id)
        if roomform:

            db.session.delete(roomform)
            db.session.commit()
            return "Xóa dòng dữ liệu thành công!"
        else:
            return "Dòng dữ liệu không tồn tại!"
    else:
        return "Hủy xóa dòng dữ liệu!"

    return render_template('pay.html', roomform = roomform)
@app.route('/pay/bill/<id>', methods=['GET','POST'])
def bill(id):
    roomform = dao.get_roomform_by_id(id)
    if not roomform:
        flash("Không tìm thấy thông tin đặt phòng!")
        return redirect('/pay')
        
    if request.method == 'POST':
        try:
            current_date = date.today()
            name = request.form.get('name')
            check_in = request.form.get('check-in')
            check_out = request.form.get('check_out')
            count = request.form.get('count')
            typeroom = request.form.get('type-room')
            total = request.form.get('total')

            if all([name, check_in, check_out, count, typeroom, total]):
                # Lưu thông tin vào bảng Bill trước
                bill = Bill(
                    name=name,
                    check_in=check_in,
                    check_out=check_out,
                    count=count,
                    typeroom=typeroom,
                    total=float(total),
                    create_date=current_date
                )
                db.session.add(bill)
                db.session.commit()

                # Sau khi lưu Bill thành công mới xóa RoomForm
                if roomform:
                    db.session.delete(roomform)
                    db.session.commit()

                flash("Thanh toán thành công!")
                return redirect('/pay')
            else:
                flash("Vui lòng điền đầy đủ thông tin")
        except Exception as e:
            db.session.rollback()  # Rollback nếu có lỗi
            flash(f"Lỗi: {str(e)}")
        return redirect(f'/pay/bill/{id}')

    return render_template('bill.html', roomform=roomform)



if __name__ == '__main__':
    from app import admin

    app.run(debug=True)
