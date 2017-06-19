Problem files have the following layout:

   L W m g rot d res v
   l_1 w_1 d_1 r_1 v_1
   l_2 w_2 d_2 r_2 v_2
   ...
   l_m w_m d_m r_m v_m


   where:

   L: length of the bin
   W: width of the bin
   m: number of items

   and g, rot, d, res and v are flags (0 = no, 1 = yes)

   g: cuts must be guillotine cuts?
   rot: items could be orthogonally rotated?
   d: itens have a demand?
   res: number of occurrences of an item in a pattern is restricted?
   v: items have a value?

   l_i: length of the item i
   w_i: width of the item i
   d_i: demand of the item i
   r_i: maximum number of occurrences of the item i in a pattern
   v_i: value of the item i

OBS.: Parâmetros com valores iguais a 0, significa que não devem ser considerados