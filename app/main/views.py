
from flask import render_template,url_for,abort,redirect,request,flash
from flask_login import login_required,current_user
from . import main
from ..request import get_quote
from ..models import User,Blog,Comment
from .forms import BlogForm,CommentForm
from ..email import mail_message
from .. import db




@main.route('/')
def index():
    quote = get_quote()
    title = 'Welcome to Blog'
    return render_template('index.html',quote=quote,title=title)


@main.route('/blog/new',methods=['GET','POST'])

def blogs():
    form = BlogForm()
    if form.validate_on_submit():
        
        
        new_blog = Blog(title=form.title.data, description=form.description.data)
        #new_blog = Blog(title=title, description=description, user=current_user)
        
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('main.blogs'))
    title = 'Blog'
    return render_template('blogs.html', title=title, form=form)


@main.route('/blog/all', methods=['GET', 'POST'])

def theblog():
    blogs = Blog.query.all()
    return render_template('myblogs.html', blogs=blogs)

@main.route('/Update/<int:id>', methods=['GET', 'POST'])

def update_blog(id):
    blog = Blog.query.get_or_404(id)
    if blog.user != current_user:
        abort(403)
    form = BlogForm()
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.description = form.description.data
        db.session.commit()

        return redirect(url_for('.theblog'))
    elif request.method == 'GET':
        form.title_blog.data = blog.title_blog
        form.description.data = blog.description
    return render_template('update_blog.html', form=form)


@main.route('/view/<int:id>', methods=['GET', 'POST'])

def view(id):
    blog = Blog.query.get_or_404(id)
    blog_comments = Comment.query.filter_by(blog_id=id).all()
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        new_comment = Comment(blog_id=id, comment=comment_form.comment.data)
        new_comment.save_comment()
    return render_template('view.html', blog=blog, blog_comments=blog_comments, comment_form=comment_form)



@main.route('/delete/<int:id>', methods=['GET', 'POST'])

def delete(id):
    blog = Blog.query.filter_by(id=id).first()
    
    db.session.delete(blog)
    db.session.commit()

    return redirect(url_for('main.theblog'))

@main.route('/delete_comment/<int:comment_id>', methods=['GET', 'POST'])

def delete_comment(comment_id):
    comment =Comment.query.get_or_404(comment_id)
    if (comment.user.id) != current_user.id:
        abort(403)
    db.session.delete(comment)
    db.session.commit()
    flash('Succesfully deleted')
    return redirect (url_for('main.theblog'))