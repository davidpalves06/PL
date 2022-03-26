
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NUM PA PF\n    ABin : PA PF\n         | PA NUM ABin ABin PF\n    '
    
_lr_action_items = {'PA':([0,3,4,5,7,],[2,-1,2,2,-2,]),'$end':([1,3,7,],[0,-1,-2,]),'PF':([2,3,6,7,],[3,-1,7,-2,]),'NUM':([2,],[4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'ABin':([0,4,5,],[1,5,6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> ABin","S'",1,None,None,None),
  ('ABin -> PA PF','ABin',2,'p_gramatica','abin_sin.py',6),
  ('ABin -> PA NUM ABin ABin PF','ABin',5,'p_gramatica','abin_sin.py',7),
]
