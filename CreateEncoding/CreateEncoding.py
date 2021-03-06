from vanilla import *
from defconAppKit.windows.baseWindow import BaseWindowController

encodingL = [
'.notdef',
'.null',
'CR',
'space',
'uni00A0',
'A',
'B',
'C',
'D',
'E',
'F',
'G',
'H',
'I',
'J',
'K',
'L',
'M',
'N',
'O',
'P',
'Q',
'R',
'S',
'T',
'U',
'V',
'W',
'X',
'Y',
'Z',
'AE',
'OE',
'Lslash',
'Oslash',
'Eth',
'Thorn',

'a',
'b',
'c',
'd',
'e',
'f',
'g',
'h',
'i',
'j',
'k',
'l',
'm',
'n',
'o',
'p',
'q',
'r',
's',
't',
'u',
'v',
'w',
'x',
'y',
'z',
'ae',
'oe',
'lslash',
'oslash',
'eth',
'thorn',
'germandbls',
'dotlessi',
'dotlessj',

'fi',
'fl',
'f_f',
'f_f_i',
'f_f_l',

'f_t',
'f_b',
'f_f_b',
'f_h',
'f_f_h',
'f_k',
'f_f_k',
'f_j',
'f_f_j',
'f_f_t',
'c_t',
's_p',
's_t',

'a.sc',
'b.sc',
'c.sc',
'd.sc',
'e.sc',
'f.sc',
'g.sc',
'h.sc',
'i.sc',
'j.sc',
'k.sc',
'l.sc',
'm.sc',
'n.sc',
'o.sc',
'p.sc',
'q.sc',
'r.sc',
's.sc',
't.sc',
'u.sc',
'v.sc',
'w.sc',
'x.sc',
'y.sc',
'z.sc',
'ae.sc',
'oe.sc',
'lslash.sc',
'oslash.sc',
'eth.sc',
'thorn.sc',
'germandbls.sc',
'dotlessi.sc',
'dotlessj.sc',

'ampersand.sc',
'exclam.sc',
'question.sc',
'exclamdown.sc',
'questiondown.sc',
'parenleft.sc',
'parenright.sc',
'braceleft.sc',
'braceright.sc',
'bracketleft.sc',
'bracketright.sc',
'hyphen.sc',
'quoteleft.sc',
'quotedblleft.sc',
'quoteright.sc',
'quotedblright.sc',
'quotesingle.sc',
'quotedbl.sc',

'Aacute',
'Acircumflex',
'Adieresis',
'Agrave',
'Aring',
'Atilde',
'Abreve',
'Amacron',
'Aogonek',
'Ccedilla',
'Cacute',
'Ccaron',
'Ccircumflex',
'Cdotaccent',
'Dcaron',
'Dcroat',
'Eacute',
'Ecircumflex',
'Edieresis',
'Egrave',
'Ebreve',
'Ecaron',
'Edotaccent',
'Emacron',
'Eogonek',
'Gbreve',
'Gcircumflex',
'Gcommaaccent',
'Gdotaccent',
'Hbar',
'Hcircumflex',
'Iacute',
'Icircumflex',
'Idieresis',
'Igrave',
'Ibreve',
'Idotaccent',
'Imacron',
'Iogonek',
'Itilde',
'Jcircumflex',
'IJ',
'Kcommaaccent',
'Lacute',
'Lcaron',
'Lcommaaccent',
'Ldot',
'Ntilde',
'Nacute',
'Ncaron',
'Ncommaaccent',
'Oacute',
'Ocircumflex',
'Odieresis',
'Ograve',
'Otilde',
'Obreve',
'Ohungarumlaut',
'Omacron',
'Racute',
'Rcaron',
'Rcommaaccent',
'Scaron',
'Sacute',
'Scedilla',
'Scircumflex',
'uni0218',
'Tbar',
'Tcaron',
'uni0162',
'uni021A',
'Uacute',
'Ucircumflex',
'Udieresis',
'Ugrave',
'Ubreve',
'Uhungarumlaut',
'Umacron',
'Uogonek',
'Uring',
'Utilde',
'Wacute',
'Wcircumflex',
'Wdieresis',
'Wgrave',
'Yacute',
'Ydieresis',
'Ycircumflex',
'Ygrave',
'Zcaron',
'Zacute',
'Zdotaccent',

'aacute',
'acircumflex',
'adieresis',
'agrave',
'aring',
'atilde',
'abreve',
'amacron',
'aogonek',
'ccedilla',
'cacute',
'ccaron',
'ccircumflex',
'cdotaccent',
'dcaron',
'dcroat',
'eacute',
'ecircumflex',
'edieresis',
'egrave',
'ebreve',
'ecaron',
'edotaccent',
'emacron',
'eogonek',
'gbreve',
'gcircumflex',
'gcommaaccent',
'gdotaccent',
'hbar',
'hcircumflex',
'iacute',
'icircumflex',
'idieresis',
'igrave',
'ibreve',
'i.dot',
'imacron',
'iogonek',
'itilde',
'jcircumflex',
'ij',
'kcommaaccent',
'lacute',
'lcaron',
'lcommaaccent',
'ldot',
'ntilde',
'nacute',
'ncaron',
'ncommaaccent',
'oacute',
'ocircumflex',
'odieresis',
'ograve',
'otilde',
'obreve',
'ohungarumlaut',
'omacron',
'racute',
'rcaron',
'rcommaaccent',
'scaron',
'sacute',
'scedilla',
'scircumflex',
'uni0219',
'tbar',
'tcaron',
'uni0163',
'uni021B',
'uacute',
'ucircumflex',
'udieresis',
'ugrave',
'ubreve',
'uhungarumlaut',
'umacron',
'uogonek',
'uring',
'utilde',
'wacute',
'wcircumflex',
'wdieresis',
'wgrave',
'yacute',
'ydieresis',
'ycircumflex',
'ygrave',
'zcaron',
'zacute',
'zdotaccent',

'aacute.sc',
'acircumflex.sc',
'adieresis.sc',
'agrave.sc',
'aring.sc',
'atilde.sc',
'abreve.sc',
'amacron.sc',
'aogonek.sc',
'ccedilla.sc',
'cacute.sc',
'ccaron.sc',
'ccircumflex.sc',
'cdotaccent.sc',
'dcaron.sc',
'dcroat.sc',
'eacute.sc',
'ecircumflex.sc',
'edieresis.sc',
'egrave.sc',
'ebreve.sc',
'ecaron.sc',
'edotaccent.sc',
'emacron.sc',
'eogonek.sc',
'gbreve.sc',
'gcircumflex.sc',
'gcommaaccent.sc',
'gdotaccent.sc',
'hbar.sc',
'hcircumflex.sc',
'iacute.sc',
'icircumflex.sc',
'idieresis.sc',
'igrave.sc',
'ibreve.sc',
'i.dot.sc',
'imacron.sc',
'iogonek.sc',
'itilde.sc',
'jcircumflex.sc',
'ij.sc',
'kcommaaccent.sc',
'lacute.sc',
'lcaron.sc',
'lcommaaccent.sc',
'ldot.sc',
'ntilde.sc',
'nacute.sc',
'ncaron.sc',
'ncommaaccent.sc',
'oacute.sc',
'ocircumflex.sc',
'odieresis.sc',
'ograve.sc',
'otilde.sc',
'obreve.sc',
'ohungarumlaut.sc',
'omacron.sc',
'racute.sc',
'rcaron.sc',
'rcommaaccent.sc',
'scaron.sc',
'sacute.sc',
'scedilla.sc',
'scircumflex.sc',
'uni0219.sc',
'tbar.sc',
'tcaron.sc',
'uni0163.sc',
'uni021B.sc',
'uacute.sc',
'ucircumflex.sc',
'udieresis.sc',
'ugrave.sc',
'ubreve.sc',
'uhungarumlaut.sc',
'umacron.sc',
'uogonek.sc',
'uring.sc',
'utilde.sc',
'wacute.sc',
'wcircumflex.sc',
'wdieresis.sc',
'wgrave.sc',
'yacute.sc',
'ydieresis.sc',
'ycircumflex.sc',
'ygrave.sc',
'zcaron.sc',
'zacute.sc',
'zdotaccent.sc',

'acute',
'grave',
'circumflex',
'caron',
'tilde',
'dieresis',
'ring',
'cedilla',

'hungarumlaut',
'breve',
'macron',
'dotaccent',
'periodcentered',
'ogonek',
'commaaccent',

'caron.alt',
'revcommaaccent',

'acute.cap',
'grave.cap',
'circumflex.cap',
'caron.cap',
'tilde.cap',
'dieresis.cap',
'ring.cap',
'cedilla.cap',

'hungarumlaut.cap',
'breve.cap',
'macron.cap',
'dotaccent.cap',
'ogonek.cap',
'commaaccent.cap',
'caron.alt.cap',

'acute.sc',
'grave.sc',
'circumflex.sc',
'caron.sc',
'tilde.sc',
'dieresis.sc',
'ring.sc',
'cedilla.sc',

'hungarumlaut.sc',
'breve.sc',
'macron.sc',
'dotaccent.sc',
'ogonek.sc',
'commaaccent.sc',
'caron.alt.sc',

'period',
'comma',
'colon',
'semicolon',
'ellipsis',
'question',
'exclam',
'questiondown',
'exclamdown',
'parenleft',
'parenright',
'braceleft',
'braceright',
'bracketleft',
'bracketright',
'slash',
'backslash',
'underscore',
'hyphen',
'uni00AD',
'endash',
'emdash',
'brokenbar',
'bar',
'guillemotleft',
'guillemotright',
'guilsinglleft',
'guilsinglright',
'quotesinglbase',
'quotedblbase',
'quoteleft',
'quotedblleft',
'quoteright',
'quotedblright',
'quotesingle',
'quotedbl',
'bullet',
'ampersand',
'paragraph',
'dagger',
'daggerdbl',
'section',
'asterisk',
'trademark',
'registered',
'copyright',
'at',
'ordfeminine',
'ordmasculine',

'a.sup',
'b.sup',
'c.sup',
'd.sup',
'e.sup',
'f.sup',
'g.sup',
'h.sup',
'i.sup',
'j.sup',
'k.sup',
'l.sup',
'm.sup',
'n.sup',
'o.sup',
'p.sup',
'q.sup',
'r.sup',
's.sup',
't.sup',
'u.sup',
'v.sup',
'w.sup',
'x.sup',
'y.sup',
'z.sup',

'numbersign',
'Euro',
'dollar',
'yen',
'sterling',
'cent',
'florin',
'currency',

'zero',
'one',
'two',
'three',
'four',
'five',
'six',
'seven',
'eight',
'nine',
'zeroslash',

'numbersign.plf',
'Euro.plf',
'dollar.plf',
'yen.plf',
'sterling.plf',
'cent.plf',
'zero.plf',
'one.plf',
'two.plf',
'three.plf',
'four.plf',
'five.plf',
'six.plf',
'seven.plf',
'eight.plf',
'nine.plf',
'zeroslash.plf',

'numbersign.tlf',
'Euro.tlf',
'dollar.tlf',
'yen.tlf',
'sterling.tlf',
'cent.tlf',
'zero.tlf',
'one.tlf',
'two.tlf',
'three.tlf',
'four.tlf',
'five.tlf',
'six.tlf',
'seven.tlf',
'eight.tlf',
'nine.tlf',
'zeroslash.tlf',

'numbersign.tosf',
'Euro.tosf',
'dollar.tosf',
'yen.tosf',
'sterling.tosf',
'cent.tosf',
'zero.tosf',
'one.tosf',
'two.tosf',
'three.tosf',
'four.tosf',
'five.tosf',
'six.tosf',
'seven.tosf',
'eight.tosf',
'nine.tosf',
'zeroslash.tosf',

'numbersign.posf',
'Euro.posf',
'dollar.posf',
'yen.posf',
'sterling.posf',
'cent.posf',
'zero.posf',
'one.posf',
'two.posf',
'three.posf',
'four.posf',
'five.posf',
'six.posf',
'seven.posf',
'eight.posf',
'nine.posf',
'zeroslash.posf',

'numbersign.tscf',
'Euro.tscf',
'dollar.tscf',
'yen.tscf',
'sterling.tscf',
'cent.tscf',
'zero.tscf',
'one.tscf',
'two.tscf',
'three.tscf',
'four.tscf',
'five.tscf',
'six.tscf',
'seven.tscf',
'eight.tscf',
'nine.tscf',
'zeroslash.tscf',

'numbersign.pscf',
'Euro.pscf',
'dollar.pscf',
'yen.pscf',
'sterling.pscf',
'cent.pscf',
'zero.pscf',
'one.pscf',
'two.pscf',
'three.pscf',
'four.pscf',
'five.pscf',
'six.pscf',
'seven.pscf',
'eight.pscf',
'nine.pscf',
'zeroslash.pscf',

'percent.sc',
'perthousand.sc',

'degree',
'percent',
'perthousand',

'fraction',
'uni2215',

'zerosuperior',
'onesuperior',
'twosuperior',
'threesuperior',
'foursuperior',
'fivesuperior',
'sixsuperior',
'sevensuperior',
'eightsuperior',
'ninesuperior',

'onehalf',
'onequarter',
'threequarters',
'onethird',
'twothirds',
'oneeighth',
'threeeighths',
'fiveeighths',
'seveneighths',
'onefifth',
'twofifths',
'threefifths',
'fourfifths',
'onesixth',
'fivesixths',
'oneseventh',
'twosevenths',
'threesevenths',
'foursevenths',
'fivesevenths',
'sixsevenths',
'oneninth',
'twoninths',
'fourninths',
'fiveninths',
'sevenninths',
'eightninths',

'zeroinferior',
'oneinferior',
'twoinferior',
'threeinferior',
'fourinferior',
'fiveinferior',
'sixinferior',
'seveninferior',
'eightinferior',
'nineinferior',

'zero.numerator',
'one.numerator',
'two.numerator',
'three.numerator',
'four.numerator',
'five.numerator',
'six.numerator',
'seven.numerator',
'eight.numerator',
'nine.numerator',

'zero.denominator',
'one.denominator',
'two.denominator',
'three.denominator',
'four.denominator',
'five.denominator',
'six.denominator',
'seven.denominator',
'eight.denominator',
'nine.denominator',

'plus',
'minus',
'multiply',
'divide',
'equal',
'logicalnot',
'asciitilde',
'less',
'greater',
'plusminus',
'asciicircum',
'notequal',
'approxequal',
'lessequal',
'greaterequal',
'infinity',
'lozenge',
'radical',
'integral',
'partialdiff',
'product',
'pi',
'mu',
'summation',
'Omega',
'uni03A9',
'Delta',
'uni0394',
'uni2113',
'estimated',
'heart'
	]
	
	
encodingM = [
'.notdef',
'.null',
'CR',
'space',
'uni00A0',
'A',
'B',
'C',
'D',
'E',
'F',
'G',
'H',
'I',
'J',
'K',
'L',
'M',
'N',
'O',
'P',
'Q',
'R',
'S',
'T',
'U',
'V',
'W',
'X',
'Y',
'Z',
'AE',
'OE',
'Lslash',
'Oslash',
'Eth',
'Thorn',

'a',
'b',
'c',
'd',
'e',
'f',
'g',
'h',
'i',
'j',
'k',
'l',
'm',
'n',
'o',
'p',
'q',
'r',
's',
't',
'u',
'v',
'w',
'x',
'y',
'z',
'ae',
'oe',
'lslash',
'oslash',
'eth',
'thorn',
'germandbls',
'dotlessi',
'dotlessj',

'fi',
'fl',
'f_f',
'f_f_i',
'f_f_l',

'Aacute',
'Acircumflex',
'Adieresis',
'Agrave',
'Aring',
'Atilde',
'Abreve',
'Amacron',
'Aogonek',
'Ccedilla',
'Cacute',
'Ccaron',
'Ccircumflex',
'Cdotaccent',
'Dcaron',
'Dcroat',
'Eacute',
'Ecircumflex',
'Edieresis',
'Egrave',
'Ebreve',
'Ecaron',
'Edotaccent',
'Emacron',
'Eogonek',
'Gbreve',
'Gcircumflex',
'Gcommaaccent',
'Gdotaccent',
'Hbar',
'Hcircumflex',
'Iacute',
'Icircumflex',
'Idieresis',
'Igrave',
'Ibreve',
'Idotaccent',
'Imacron',
'Iogonek',
'Itilde',
'Jcircumflex',
'IJ',
'Kcommaaccent',
'Lacute',
'Lcaron',
'Lcommaaccent',
'Ldot',
'Ntilde',
'Nacute',
'Ncaron',
'Ncommaaccent',
'Oacute',
'Ocircumflex',
'Odieresis',
'Ograve',
'Otilde',
'Obreve',
'Ohungarumlaut',
'Omacron',
'Racute',
'Rcaron',
'Rcommaaccent',
'Scaron',
'Sacute',
'Scedilla',
'Scircumflex',
'uni0218',
'Tbar',
'Tcaron',
'uni0162',
'uni021A',
'Uacute',
'Ucircumflex',
'Udieresis',
'Ugrave',
'Ubreve',
'Uhungarumlaut',
'Umacron',
'Uogonek',
'Uring',
'Utilde',
'Wacute',
'Wcircumflex',
'Wdieresis',
'Wgrave',
'Yacute',
'Ydieresis',
'Ycircumflex',
'Ygrave',
'Zcaron',
'Zacute',
'Zdotaccent',

'aacute',
'acircumflex',
'adieresis',
'agrave',
'aring',
'atilde',
'abreve',
'amacron',
'aogonek',
'ccedilla',
'cacute',
'ccaron',
'ccircumflex',
'cdotaccent',
'dcaron',
'dcroat',
'eacute',
'ecircumflex',
'edieresis',
'egrave',
'ebreve',
'ecaron',
'edotaccent',
'emacron',
'eogonek',
'gbreve',
'gcircumflex',
'gcommaaccent',
'gdotaccent',
'hbar',
'hcircumflex',
'iacute',
'icircumflex',
'idieresis',
'igrave',
'ibreve',
'i.dot',
'imacron',
'iogonek',
'itilde',
'jcircumflex',
'ij',
'kcommaaccent',
'lacute',
'lcaron',
'lcommaaccent',
'ldot',
'ntilde',
'nacute',
'ncaron',
'ncommaaccent',
'oacute',
'ocircumflex',
'odieresis',
'ograve',
'otilde',
'obreve',
'ohungarumlaut',
'omacron',
'racute',
'rcaron',
'rcommaaccent',
'scaron',
'sacute',
'scedilla',
'scircumflex',
'uni0219',
'tbar',
'tcaron',
'uni0163',
'uni021B',
'uacute',
'ucircumflex',
'udieresis',
'ugrave',
'ubreve',
'uhungarumlaut',
'umacron',
'uogonek',
'uring',
'utilde',
'wacute',
'wcircumflex',
'wdieresis',
'wgrave',
'yacute',
'ydieresis',
'ycircumflex',
'ygrave',
'zcaron',
'zacute',
'zdotaccent',

'acute',
'grave',
'circumflex',
'caron',
'tilde',
'dieresis',
'ring',
'cedilla',

'hungarumlaut',
'breve',
'macron',
'dotaccent',
'periodcentered',
'ogonek',
'commaaccent',

'caron.alt',
'revcommaaccent',

'acute.cap',
'grave.cap',
'circumflex.cap',
'caron.cap',
'tilde.cap',
'dieresis.cap',
'ring.cap',
'cedilla.cap',

'hungarumlaut.cap',
'breve.cap',
'macron.cap',
'dotaccent.cap',
'ogonek.cap',
'commaaccent.cap',
'caron.alt.cap',

'period',
'comma',
'colon',
'semicolon',
'ellipsis',
'question',
'exclam',
'questiondown',
'exclamdown',
'parenleft',
'parenright',
'braceleft',
'braceright',
'bracketleft',
'bracketright',
'slash',
'backslash',
'underscore',
'hyphen',
'uni00AD',
'endash',
'emdash',
'brokenbar',
'bar',
'guillemotleft',
'guillemotright',
'guilsinglleft',
'guilsinglright',
'quotesinglbase',
'quotedblbase',
'quoteleft',
'quotedblleft',
'quoteright',
'quotedblright',
'quotesingle',
'quotedbl',
'bullet',
'ampersand',
'paragraph',
'dagger',
'daggerdbl',
'section',
'asterisk',
'trademark',
'registered',
'copyright',
'at',
'ordfeminine',
'ordmasculine',

'numbersign',
'Euro',
'dollar',
'yen',
'sterling',
'cent',
'florin',
'currency',

'zero',
'one',
'two',
'three',
'four',
'five',
'six',
'seven',
'eight',
'nine',
'zeroslash',

'numbersign.plf',
'Euro.plf',
'dollar.plf',
'yen.plf',
'sterling.plf',
'cent.plf',
'zero.plf',
'one.plf',
'two.plf',
'three.plf',
'four.plf',
'five.plf',
'six.plf',
'seven.plf',
'eight.plf',
'nine.plf',
'zeroslash.plf',

'numbersign.tlf',
'Euro.tlf',
'dollar.tlf',
'yen.tlf',
'sterling.tlf',
'cent.tlf',
'zero.tlf',
'one.tlf',
'two.tlf',
'three.tlf',
'four.tlf',
'five.tlf',
'six.tlf',
'seven.tlf',
'eight.tlf',
'nine.tlf',
'zeroslash.tlf',

'numbersign.tosf',
'Euro.tosf',
'dollar.tosf',
'yen.tosf',
'sterling.tosf',
'cent.tosf',
'zero.tosf',
'one.tosf',
'two.tosf',
'three.tosf',
'four.tosf',
'five.tosf',
'six.tosf',
'seven.tosf',
'eight.tosf',
'nine.tosf',
'zeroslash.tosf',

'numbersign.posf',
'Euro.posf',
'dollar.posf',
'yen.posf',
'sterling.posf',
'cent.posf',
'zero.posf',
'one.posf',
'two.posf',
'three.posf',
'four.posf',
'five.posf',
'six.posf',
'seven.posf',
'eight.posf',
'nine.posf',
'zeroslash.posf',

'degree',
'percent',
'perthousand',

'fraction',
'uni2215',

'zerosuperior',
'onesuperior',
'twosuperior',
'threesuperior',
'foursuperior',
'fivesuperior',
'sixsuperior',
'sevensuperior',
'eightsuperior',
'ninesuperior',

'onehalf',
'onequarter',
'threequarters',
'onethird',
'twothirds',
'oneeighth',
'threeeighths',
'fiveeighths',
'seveneighths',
'onefifth',
'twofifths',
'threefifths',
'fourfifths',
'onesixth',
'fivesixths',
'oneseventh',
'twosevenths',
'threesevenths',
'foursevenths',
'fivesevenths',
'sixsevenths',
'oneninth',
'twoninths',
'fourninths',
'fiveninths',
'sevenninths',
'eightninths',

'zeroinferior',
'oneinferior',
'twoinferior',
'threeinferior',
'fourinferior',
'fiveinferior',
'sixinferior',
'seveninferior',
'eightinferior',
'nineinferior',

'zero.numerator',
'one.numerator',
'two.numerator',
'three.numerator',
'four.numerator',
'five.numerator',
'six.numerator',
'seven.numerator',
'eight.numerator',
'nine.numerator',

'zero.denominator',
'one.denominator',
'two.denominator',
'three.denominator',
'four.denominator',
'five.denominator',
'six.denominator',
'seven.denominator',
'eight.denominator',
'nine.denominator',

'plus',
'minus',
'multiply',
'divide',
'equal',
'logicalnot',
'asciitilde',
'less',
'greater',
'plusminus',
'asciicircum',
'notequal',
'approxequal',
'lessequal',
'greaterequal',
'infinity',
'lozenge',
'radical',
'integral',
'partialdiff',
'product',
'pi',
'mu',
'summation',
'Omega',
'uni03A9',
'Delta',
'uni0394',
'uni2113',
'estimated',
'heart'
	]
	
encodingS = [
'.notdef',
'.null',
'CR',
'space',
'uni00A0',
'A',
'B',
'C',
'D',
'E',
'F',
'G',
'H',
'I',
'J',
'K',
'L',
'M',
'N',
'O',
'P',
'Q',
'R',
'S',
'T',
'U',
'V',
'W',
'X',
'Y',
'Z',
'AE',
'OE',
'Lslash',
'Oslash',
'Eth',
'Thorn',
'a',
'b',
'c',
'd',
'e',
'f',
'g',
'h',
'i',
'j',
'k',
'l',
'm',
'n',
'o',
'p',
'q',
'r',
's',
't',
'u',
'v',
'w',
'x',
'y',
'z',
'ae',
'oe',
'lslash',
'oslash',
'eth',
'thorn',
'germandbls',
'dotlessi',
'dotlessj',
'fi',
'fl',
'Aacute',
'Acircumflex',
'Adieresis',
'Agrave',
'Aring',
'Atilde',
'Abreve',
'Amacron',
'Aogonek',
'Ccedilla',
'Cacute',
'Ccaron',
'Ccircumflex',
'Cdotaccent',
'Dcaron',
'Dcroat',
'Eacute',
'Ecircumflex',
'Edieresis',
'Egrave',
'Ebreve',
'Ecaron',
'Edotaccent',
'Emacron',
'Eogonek',
'Gbreve',
'Gcircumflex',
'Gcommaaccent',
'Gdotaccent',
'Hbar',
'Hcircumflex',
'Iacute',
'Icircumflex',
'Idieresis',
'Igrave',
'Ibreve',
'Idotaccent',
'Imacron',
'Iogonek',
'Itilde',
'Jcircumflex',
'IJ',
'Kcommaaccent',
'Lacute',
'Lcaron',
'Lcommaaccent',
'Ldot',
'Ntilde',
'Nacute',
'Ncaron',
'Ncommaaccent',
'Oacute',
'Ocircumflex',
'Odieresis',
'Ograve',
'Otilde',
'Obreve',
'Ohungarumlaut',
'Omacron',
'Racute',
'Rcaron',
'Rcommaaccent',
'Scaron',
'Sacute',
'Scedilla',
'Scircumflex',
'uni0218',
'Tbar',
'Tcaron',
'uni0162',
'uni021A',
'Uacute',
'Ucircumflex',
'Udieresis',
'Ugrave',
'Ubreve',
'Uhungarumlaut',
'Umacron',
'Uogonek',
'Uring',
'Utilde',
'Wacute',
'Wcircumflex',
'Wdieresis',
'Wgrave',
'Yacute',
'Ydieresis',
'Ycircumflex',
'Ygrave',
'Zcaron',
'Zacute',
'Zdotaccent',
'aacute',
'acircumflex',
'adieresis',
'agrave',
'aring',
'atilde',
'abreve',
'amacron',
'aogonek',
'ccedilla',
'cacute',
'ccaron',
'ccircumflex',
'cdotaccent',
'dcaron',
'dcroat',
'eacute',
'ecircumflex',
'edieresis',
'egrave',
'ebreve',
'ecaron',
'edotaccent',
'emacron',
'eogonek',
'gbreve',
'gcircumflex',
'gcommaaccent',
'gdotaccent',
'hbar',
'hcircumflex',
'iacute',
'icircumflex',
'idieresis',
'igrave',
'ibreve',
'i.dot',
'imacron',
'iogonek',
'itilde',
'jcircumflex',
'ij',
'kcommaaccent',
'lacute',
'lcaron',
'lcommaaccent',
'ldot',
'ntilde',
'nacute',
'ncaron',
'ncommaaccent',
'oacute',
'ocircumflex',
'odieresis',
'ograve',
'otilde',
'obreve',
'ohungarumlaut',
'omacron',
'racute',
'rcaron',
'rcommaaccent',
'scaron',
'sacute',
'scedilla',
'scircumflex',
'uni0219',
'tbar',
'tcaron',
'uni0163',
'uni021B',
'uacute',
'ucircumflex',
'udieresis',
'ugrave',
'ubreve',
'uhungarumlaut',
'umacron',
'uogonek',
'uring',
'utilde',
'wacute',
'wcircumflex',
'wdieresis',
'wgrave',
'yacute',
'ydieresis',
'ycircumflex',
'ygrave',
'zcaron',
'zacute',
'zdotaccent',
'acute',
'grave',
'circumflex',
'caron',
'tilde',
'dieresis',
'ring',
'cedilla',
'hungarumlaut',
'breve',
'macron',
'dotaccent',
'periodcentered',
'ogonek',
'commaaccent',
'caron.alt',
'revcommaaccent',
'acute.cap',
'grave.cap',
'circumflex.cap',
'caron.cap',
'tilde.cap',
'dieresis.cap',
'ring.cap',
'cedilla.cap',
'hungarumlaut.cap',
'breve.cap',
'macron.cap',
'dotaccent.cap',
'ogonek.cap',
'commaaccent.cap',
'caron.alt.cap',
'period',
'comma',
'colon',
'semicolon',
'ellipsis',
'question',
'exclam',
'questiondown',
'exclamdown',
'parenleft',
'parenright',
'braceleft',
'braceright',
'bracketleft',
'bracketright',
'slash',
'backslash',
'underscore',
'hyphen',
'uni00AD',
'endash',
'emdash',
'brokenbar',
'bar',
'guillemotleft',
'guillemotright',
'guilsinglleft',
'guilsinglright',
'quotesinglbase',
'quotedblbase',
'quoteleft',
'quotedblleft',
'quoteright',
'quotedblright',
'quotesingle',
'quotedbl',
'bullet',
'ampersand',
'paragraph',
'dagger',
'daggerdbl',
'section',
'asterisk',
'trademark',
'registered',
'copyright',
'at',
'ordfeminine',
'ordmasculine',
'numbersign',
'Euro',
'dollar',
'yen',
'sterling',
'cent',
'florin',
'currency',
'zero',
'one',
'two',
'three',
'four',
'five',
'six',
'seven',
'eight',
'nine',
'degree',
'percent',
'perthousand',
'fraction',
'uni2215',
'onesuperior',
'twosuperior',
'threesuperior',
'foursuperior',
'onehalf',
'onequarter',
'threequarters',
'plus',
'minus',
'multiply',
'divide',
'equal',
'logicalnot',
'asciitilde',
'less',
'greater',
'plusminus',
'asciicircum',
'notequal',
'approxequal',
'lessequal',
'greaterequal',
'infinity',
'lozenge',
'radical',
'integral',
'partialdiff',
'product',
'pi',
'mu',
'summation',
'Omega',
'uni03A9',
'Delta',
'uni0394',
'uni2113',
'estimated',
'heart'

]

class Process(BaseWindowController):

	def __init__(self):
		self.w = FloatingWindow((310, 200))
		self.w.textBox = TextBox((10, 10, -10, 16), "GlyphSet", sizeStyle = "regular", alignment = "center")
		self.w.textBoxEncodingS = CheckBox((10, 40, -10, 20), "Encoding S", sizeStyle = "small", 
											callback=self.textBoxEncodingSCallback, value = False)
		self.w.textBoxEncodingM = CheckBox((10, 70, -10, 20), "Encoding M", sizeStyle = "small", 
											callback=self.textBoxEncodingMCallback, value = False)
		self.w.textBoxEncodingL = CheckBox((10, 100, -10, 20), "Encoding L", sizeStyle = "small", 
											callback=self.textBoxEncodingLCallback, value = False)
		self.w.textBoxEncodingNone = CheckBox((10, 130, -10, 20), "None", sizeStyle = "small", 
											callback=self.textBoxEncodingNoneCallback, value = False)
		self.w.buttonApply = Button((10, -20, 90, 15), "Apply", sizeStyle = "small", callback=self.showProgress)
		self.w.buttonClose = Button((210, -20, 90, 15), "Close", sizeStyle = "small", callback=self.closeWindow)
		self.w.center()
		self.w.open()
	
	def closeWindow(self, sender):
		self.w.close()
		
	def textBoxEncodingSCallback(self, sender):
		if sender.get():
			self.w.textBoxEncodingM.set(False)
			self.w.textBoxEncodingL.set(False)
			self.w.textBoxEncodingNone.set(False)
		
	def textBoxEncodingMCallback(self, sender):
		if sender.get():
			self.w.textBoxEncodingS.set(False)
			self.w.textBoxEncodingL.set(False)
			self.w.textBoxEncodingNone.set(False)
	
	def textBoxEncodingLCallback(self, sender):
		if sender.get():
			self.w.textBoxEncodingS.set(False)
			self.w.textBoxEncodingM.set(False)
			self.w.textBoxEncodingNone.set(False)
	
	def textBoxEncodingNoneCallback(self, sender):
		if sender.get():
			self.w.textBoxEncodingS.set(False)
			self.w.textBoxEncodingM.set(False)
			self.w.textBoxEncodingL.set(False)
	
	def showProgress(self, sender):
		self.progress = self.startProgress("Updating Encoding...")
		if self.w.textBoxEncodingL.get():
			f.glyphOrder = encodingL
			self.progress.close()
		elif self.w.textBoxEncodingM.get():
			f.glyphOrder = encodingM
			self.progress.close()
		elif self.w.textBoxEncodingS.get():
			f.glyphOrder = encodingS
			self.progress.close()
		elif self.w.textBoxEncodingNone.get():
			f.glyphOrder = []
			self.progress.close()
		self.w.close()


f = CurrentFont()
Process()