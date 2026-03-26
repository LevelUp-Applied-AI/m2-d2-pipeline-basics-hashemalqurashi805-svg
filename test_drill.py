"""
Module 2 — Drill 2: Learner Test File

Write your two pytest test functions below.
The autograder will run these as part of the CI check.
"""

import pandas as pd
import numpy as np
from drill_functions import clean_column, compute_revenue


def test_clean_column():
   # 1. إنشاء بيانات تجريبية تحتوي على NaN
    series = pd.Series([1, 2, np.nan, 4, 5]) 
    # الوسيط (Median) هنا هو 3.0
    
    # 2. استدعاء الدالة
    result = clean_column(series)
    
    # 3. التأكد من اختفاء القيم المفقودة
    assert result.isna().sum() == 0
    
    # 4. التأكد أن القيمة تم استبدالها بالوسيط الصحيح (3.0)
    assert result[2] == 3.0


def test_compute_revenue():
    # 1. إنشاء بيانات للكمية والسعر
    quantity = pd.Series([2, 10])
    price = pd.Series([5, 3])
    
    # 2. استدعاء الدالة
    revenue = compute_revenue(quantity, price)
    
    # 3. التأكد أن النتيجة مطابقة للضرب (2*5=10 و 10*3=30)
    expected = pd.Series([10, 30])
    pd.testing.assert_series_equal(revenue, expected)