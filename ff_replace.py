import fontforge
import subprocess

glyph_names = [
  'a', 'aogonek', 'b', 'c', 'cacute', 'd', 'e', 'eogonek', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'lslash', 'm', 'n', 'nacute', 'o', 'oacute', 'p', 'q', 'r', 's', 'sacute', 't', 'u', 'v', 'w', 'glyph92', 'y', 'z', 'zdotaccent', 'zacute',
  'A', 'Aogonek', 'B', 'C', 'Cacute', 'D', 'E', 'Eogonek', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Lslash', 'M', 'N', 'Nacute', 'O', 'Oacute', 'P', 'Q', 'R', 'S', 'Sacute', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Zdotaccent', 'Zacute',
  'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
  'cacute.loclPLK', 'nacute.loclPLK', 'oacute.loclPLK', 'sacute.loclPLK', 'zacute.loclPLK',
  'Cacute.loclPLK', 'Nacute.loclPLK', 'Oacute.loclPLK', 'Sacute.loclPLK', 'Zacute.loclPLK',    
  ]

font = fontforge.activeFont()

for name in glyph_names:
  i = glyph_names.index(name.split('.')[0])
  glyph = font[name]
  
  glyph.unlinkThisGlyph()
  glyph.clear()
  glyph.width = 1210
  
  subprocess.run(['inkscape', '/tmp/glify.svg', '-o', '/tmp/glif.svg', '--pages', str(i+1)])
  glyph.importOutlines('/tmp/glif.svg')
