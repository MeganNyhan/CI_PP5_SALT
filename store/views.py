import random
import string

import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from djano.utils import timezone
from django.views.generic import ListView, DetailView, View

from .models import UserProfile, Item, OrderItem, Order, Address

# Create your views here.

