from app import app, db
from flask import render_template, g, redirect, url_for, flash
from app.forms import AddCall, SelectReport, SelectShop, SelectFranchise
from app.models import Calls


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
	calls = Calls.query.order_by('date desc').all()
	return render_template('index.html', calls = calls)


@app.route('/calls', methods=['GET', 'POST'])
def addcall():
    form = AddCall()
    # #add logic to insert data into the database.
    # 	redirect('/')
    if form.validate_on_submit():
        new_call = Calls(date = form.date.data,
        			caller = form.caller.data,
        			phone = form.phone.data,
        			franchise = form.franchise.data,
        			location = form.location.data,
        			downtime = form.downtime.data,
        			plant_num = form.plant_num.data,
        			machine = form.machine.data,
        			tech = form.tech.data,
        			problem = form.problem.data,
        			comment = form.comment.data) 
        db.session.add(new_call)
        db.session.commit()
        flash('data committed!')
    	return redirect(url_for('index'))
    return render_template('calls.html', form=form)

@app.route('/reports', methods=['GET','POST'])
def reports():
    form = SelectReport()
    if form.validate_on_submit():       
        if form.report_type.data == 'all':
            return redirect(url_for('all'))
        elif form.report_type.data == 'shop':
            return redirect(url_for('shop'))
        elif form.report_type.data == 'franchise':
            return redirect(url_for('franchise'))

    return render_template('reports.html', form=form)


@app.route('/all', methods=['GET','POST'])
def all():
    calls = Calls.query.order_by('date desc').all()
    return render_template('all.html', calls=calls)


@app.route('/shop', methods=['GET','POST'])
def shop():
    form = SelectShop()
    shop_num = form.shop.data
    if form.validate_on_submit():
        return redirect(url_for('by_num', shop_num=shop_num))
    return render_template('shop.html', form = form)


@app.route('/by_num/<shop_num>', methods = ['GET','POST'])
def by_num(shop_num):
    lst = Calls.query.filter_by(plant_num=shop_num).all()
    return render_template('by_num.html', shop=shop_num, calls=lst)


@app.route('/franchise', methods=['GET','POST'])
def franchise():
    form = SelectFranchise()
    franchise = form.franchise.data
    if form.validate_on_submit():
        return redirect(url_for('by_franchise', franchise=franchise))
    return render_template('franchise.html', form=form)


@app.route('/by_franchise/<franchise>', methods=['GET','POST'])
def by_franchise(franchise):
    lst = Calls.query.filter_by(franchise = franchise).all()
    return render_template('by_franchise.html',franchise=franchise, calls=lst)
    