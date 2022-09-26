from flask import Flask, render_template, request, redirect
from users_app.models.users import User

app = Flask(__name__)
