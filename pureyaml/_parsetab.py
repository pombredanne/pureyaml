
# _parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '3FDDB538612AB4BA5C3D04E00346F1BD'
    
_lr_action_items = {'DEDENT':([1,4,6,7,9,14,15,17,20,21,23,25,26,29,30,31,32,33,],[-9,-8,-17,-6,-7,-13,-10,-11,30,-14,-16,-15,-4,-19,-5,-12,-3,-18,]),'LITERAL_INDICATOR_START':([0,1,3,4,5,6,7,8,9,10,11,12,14,15,17,21,22,23,24,25,26,29,30,31,32,33,],[13,13,13,-8,13,-17,-6,13,-7,13,13,-1,-13,-10,-11,-14,-2,-16,13,-15,-4,-19,-5,-12,-3,-18,]),'FOLD_INDICATOR_START':([0,1,3,4,5,6,7,8,9,10,11,12,14,15,17,21,22,23,24,25,26,29,30,31,32,33,],[2,2,2,-8,2,-17,-6,2,-7,2,2,-1,-13,-10,-11,-14,-2,-16,2,-15,-4,-19,-5,-12,-3,-18,]),'INDENT':([0,1,3,4,5,6,7,9,11,12,14,15,17,21,22,23,25,26,29,30,31,32,33,],[3,-9,3,-8,3,-17,-6,-7,3,-1,-13,-10,-11,-14,-2,-16,-15,-4,-19,-5,-12,-3,-18,]),'LITERAL_INDICATOR_END':([19,27,28,],[-20,33,-21,]),'MAP_INDICATOR':([6,9,16,23,29,33,],[-17,24,24,-16,-19,-18,]),'FOLD_INDICATOR_END':([18,19,28,],[29,-20,-21,]),'CAST_TYPE':([0,1,3,4,5,6,7,8,9,10,11,12,14,15,17,21,22,23,24,25,26,29,30,31,32,33,],[8,8,8,-8,8,-17,-6,8,-7,8,8,-1,-13,-10,-11,-14,-2,-16,8,-15,-4,-19,-5,-12,-3,-18,]),'SCALAR':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,],[6,6,19,6,-8,6,-17,-6,6,-7,6,6,-1,19,-13,-10,-11,28,-20,-14,-2,-16,6,-15,-4,28,-21,-19,-5,-12,-3,-18,]),'SEQUENCE_INDICATOR':([0,1,3,4,5,6,7,9,11,12,14,15,17,21,22,23,25,26,29,30,31,32,33,],[10,-9,10,10,10,-17,-6,-7,10,-1,-13,-10,-11,-14,-2,-16,-15,-4,-19,-5,-12,-3,-18,]),'DOC_INDICATOR_START':([0,1,3,4,5,6,7,9,11,12,14,15,17,21,22,23,25,26,29,30,31,32,33,],[11,-9,11,-8,11,-17,-6,-7,11,-1,-13,-10,-11,-14,-2,-16,-15,-4,-19,-5,-12,-3,-18,]),'$end':([1,4,5,6,7,9,12,14,15,17,21,22,23,25,26,29,30,31,32,33,],[-9,-8,0,-17,-6,-7,-1,-13,-10,-11,-14,-2,-16,-15,-4,-19,-5,-12,-3,-18,]),'DOC_INDICATOR_END':([1,4,6,7,9,14,15,17,21,23,25,26,29,30,31,32,33,],[-9,-8,-17,-6,-7,-13,-10,-11,-14,-16,-15,32,-19,-5,-12,-3,-18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'map':([0,3,5,11,],[1,1,1,1,]),'sequence':([0,3,5,11,],[4,4,4,4,]),'doc':([0,3,5,11,],[12,20,22,26,]),'collection':([0,3,5,11,],[7,7,7,7,]),'scalar':([0,1,3,5,8,10,11,24,],[9,16,9,9,23,25,9,31,]),'docs':([0,],[5,]),'sequence_item':([0,3,4,5,11,],[14,14,21,14,14,]),'map_item':([0,1,3,5,11,],[15,17,15,15,15,]),'scalar_group':([2,13,],[18,27,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> docs","S'",1,None,None,None),
  ('docs -> doc','docs',1,'p_docs_last','grammar.py',246),
  ('docs -> docs doc','docs',2,'p_docs_init','grammar.py',253),
  ('doc -> DOC_INDICATOR_START doc DOC_INDICATOR_END','doc',3,'p_doc_indent','grammar.py',267),
  ('doc -> DOC_INDICATOR_START doc','doc',2,'p_doc_indent','grammar.py',268),
  ('doc -> INDENT doc DEDENT','doc',3,'p_doc_indent','grammar.py',269),
  ('doc -> collection','doc',1,'p_doc','grammar.py',276),
  ('doc -> scalar','doc',1,'p_doc','grammar.py',277),
  ('collection -> sequence','collection',1,'p_collection','grammar.py',284),
  ('collection -> map','collection',1,'p_collection','grammar.py',285),
  ('map -> map_item','map',1,'p_map_last','grammar.py',292),
  ('map -> map map_item','map',2,'p_map_init','grammar.py',299),
  ('map_item -> scalar MAP_INDICATOR scalar','map_item',3,'p_map_item','grammar.py',306),
  ('sequence -> sequence_item','sequence',1,'p_sequence_last','grammar.py',312),
  ('sequence -> sequence sequence_item','sequence',2,'p_sequence_init','grammar.py',319),
  ('sequence_item -> SEQUENCE_INDICATOR scalar','sequence_item',2,'p_sequence_item','grammar.py',326),
  ('scalar -> CAST_TYPE scalar','scalar',2,'p_scalar_explicit_cast','grammar.py',333),
  ('scalar -> SCALAR','scalar',1,'p_scalar','grammar.py',340),
  ('scalar -> LITERAL_INDICATOR_START scalar_group LITERAL_INDICATOR_END','scalar',3,'p_scalar_literal','grammar.py',347),
  ('scalar -> FOLD_INDICATOR_START scalar_group FOLD_INDICATOR_END','scalar',3,'p_scalar_folded','grammar.py',354),
  ('scalar_group -> SCALAR','scalar_group',1,'p_scalar_group','grammar.py',363),
  ('scalar_group -> scalar_group SCALAR','scalar_group',2,'p_scalar_group','grammar.py',364),
]
