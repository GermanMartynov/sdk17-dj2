from django.conf.urls import url
from django.urls import path, re_path, include

from . import views

urlpatterns = [
    # main page
    path('', views.sudoku_main_page, name='puzzle_main_menu_url'),

    # new random puzzle
    path('puzzle/new/', views.new_puzzle, name='new_random_puzzle_url'),

    # show current puzzle
    path('puzzle/', views.show_puzzle, name='show_puzzle_url'),

    # установить значение ячейки
    re_path(r'^puzzle/(?P<indx>\d{1,2})/(?P<value>\d{1})/$', views.set_puzzle_value),

    path('puzzle/swich_marks/', views.on_off_marks, name='swich_marks_url'),
    path('puzzle/load/', views.load_base_tables, name='load_tables_from_file_url'),
    path('puzzle/empty/', views.new_empty_puzzle, name='empty_puzzle_url'),
    path('puzzle/mix/', views.mix_puzzle, name='mix_puzzle_url'),
    path('puzzle/mix/undo', views.undo_mix_puzzle, name='undo_mix_puzzle_url'),
    path('puzzle/relabel/', views.relabe_puzzle, name='relabe_puzzle_url'),
    path('puzzle/relabel/undo/', views.undo_relabeling_puzzle, name='undo_relabeling_puzzle_url'),
    path('puzzle/solve/', views.solve_puzzle, name='solve_puzzle_url'),

]
