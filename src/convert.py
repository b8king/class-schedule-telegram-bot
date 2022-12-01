# -*- coding: utf-8 -*-
from openpyxl import load_workbook
import pyexcel as p
import openpyxl
from PIL import Image, ImageDraw, ImageFont
import time
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
from socket import timeout
import datetime
from src import branch

path_sample='background/sample.png'
font_sample='font/1.ttf'
image_output='photo.png'
counter = 0

def get_conversion():
    start_time = time.time()
    wb = openpyxl.load_workbook('data/document/xlsx.xlsx')
    sheet2 = wb['ИСиП, ИС']
    v7=sheet2['W7'].value
    v8=sheet2['W8'].value
    v9=sheet2['W9'].value
    v10=sheet2['W10'].value
    v11=sheet2['W11'].value
    v12=sheet2['W12'].value
    v13=sheet2['W13'].value
    v14=sheet2['W14'].value
    v15=sheet2['W15'].value
    v16=sheet2['W16'].value
    v17=sheet2['W17'].value
    v18=sheet2['W18'].value
    v19=sheet2['W19'].value
    v21=sheet2['W21'].value
    v22=sheet2['W22'].value
    v23=sheet2['W23'].value
    v24=sheet2['W24'].value
    v25=sheet2['W25'].value
    v26=sheet2['W26'].value
    v27=sheet2['W27'].value
    v28=sheet2['W28'].value
    v29=sheet2['W29'].value
    v30=sheet2['W30'].value
    v31=sheet2['W31'].value
    v32=sheet2['W32'].value
    v33=sheet2['W33'].value
    v34=sheet2['W34'].value
    v35=sheet2['W35'].value
    v36=sheet2['W36'].value
    v37=sheet2['W37'].value
    v38=sheet2['W38'].value
    v39=sheet2['W39'].value
    v40=sheet2['W40'].value
    v41=sheet2['W41'].value
    v42=sheet2['W42'].value
    v43=sheet2['W43'].value
    v44=sheet2['W44'].value
    v45=sheet2['W45'].value
    v46=sheet2['W46'].value
    v47=sheet2['W47'].value
    v48=sheet2['W48'].value
    v49=sheet2['W49'].value
    v50=sheet2['W50'].value
    v51=sheet2['W51'].value
    v52=sheet2['W52'].value
    v53=sheet2['W53'].value
    v54=sheet2['W54'].value
    v55=sheet2['W55'].value
    v56=sheet2['W56'].value
    v57=sheet2['W57'].value
    v58=sheet2['W58'].value
    v59=sheet2['W59'].value
    v60=sheet2['W60'].value
    v61=sheet2['W61'].value
    v62=sheet2['W62'].value
    v63=sheet2['W63'].value
    v64=sheet2['W64'].value
    v65=sheet2['W65'].value
    v66=sheet2['W66'].value
    v67=sheet2['W67'].value
    v68=sheet2['W68'].value
    v69=sheet2['W69'].value
    v70=sheet2['W70'].value
    v71=sheet2['W71'].value
    v72=sheet2['W72'].value
    v73=sheet2['W73'].value
    v74=sheet2['W74'].value
    v75=sheet2['W75'].value
    v76=sheet2['W76'].value
    v77=sheet2['W77'].value
    v78=sheet2['W78'].value
    v79=sheet2['W79'].value
    v80=sheet2['W80'].value
    v81=sheet2['W81'].value
    v82=sheet2['W82'].value
    v83=sheet2['W83'].value
    v84=sheet2['W84'].value
    v85=sheet2['W85'].value
    x7=sheet2['X7'].value
    x8=sheet2['X8'].value
    x9=sheet2['X9'].value
    x10=sheet2['X10'].value
    x11=sheet2['X11'].value
    x12=sheet2['X12'].value
    x13=sheet2['X13'].value
    x14=sheet2['X14'].value
    x15=sheet2['X15'].value
    x16=sheet2['X16'].value
    x17=sheet2['X17'].value
    x18=sheet2['X18'].value
    x19=sheet2['X19'].value
    x21=sheet2['X21'].value
    x22=sheet2['X22'].value
    x23=sheet2['X23'].value
    x24=sheet2['X24'].value
    x25=sheet2['X25'].value
    x26=sheet2['X26'].value
    x27=sheet2['X27'].value
    x28=sheet2['X28'].value
    x29=sheet2['X29'].value
    x30=sheet2['X30'].value
    x31=sheet2['X31'].value
    x32=sheet2['X32'].value
    x33=sheet2['X33'].value
    x34=sheet2['X34'].value
    x35=sheet2['X35'].value
    x36=sheet2['X36'].value
    x37=sheet2['X37'].value
    x38=sheet2['X38'].value
    x39=sheet2['X39'].value
    x40=sheet2['X40'].value
    x41=sheet2['X41'].value
    x42=sheet2['X42'].value
    x43=sheet2['X43'].value
    x44=sheet2['X44'].value
    x45=sheet2['X45'].value
    x46=sheet2['X46'].value
    x47=sheet2['X47'].value
    x48=sheet2['X48'].value
    x49=sheet2['X49'].value
    x50=sheet2['X50'].value
    x51=sheet2['X51'].value
    x52=sheet2['X52'].value
    x53=sheet2['X53'].value
    x54=sheet2['X54'].value
    x55=sheet2['X55'].value
    x56=sheet2['X56'].value
    x57=sheet2['X57'].value
    x58=sheet2['X58'].value
    x59=sheet2['X59'].value
    x60=sheet2['X60'].value
    x61=sheet2['X61'].value
    x62=sheet2['X62'].value
    x63=sheet2['X63'].value
    x64=sheet2['X64'].value
    x65=sheet2['X65'].value
    x66=sheet2['X66'].value
    x67=sheet2['X67'].value
    x68=sheet2['X68'].value
    x69=sheet2['X69'].value
    x70=sheet2['X70'].value
    x71=sheet2['X71'].value
    x72=sheet2['X72'].value
    x73=sheet2['X73'].value
    x74=sheet2['X74'].value
    x75=sheet2['X75'].value
    x76=sheet2['X76'].value
    x77=sheet2['X77'].value
    x78=sheet2['X78'].value
    x79=sheet2['X79'].value
    x80=sheet2['X80'].value
    x81=sheet2['X81'].value
    x82=sheet2['X82'].value
    x83=sheet2['X83'].value
    x84=sheet2['X84'].value
    x85=sheet2['X85'].value
    #если нет пар
    if v8 == None:
        v8= ' '
    if v9 == None:
        v9= ' '
    if v10 == None:
        v10= ' '
    if v11 == None:
        v11= ' '
    if v12 == None:
        v12= ' '
    if v13 == None:
        v13= ' '
    if v14 == None:
        v14= ' '
    if v15 == None:
        v15= ' '
    if v16 == None:
        v16= ' '
    if v17 == None:
        v17= ' '
    if v18 == None:
        v18= ' '
    if v19 == None:
        v19= ' '
    if v21 == None:
        v21=' '    
    if v22 == None:
        v22=' '    
    if v23 == None:
        v23=' '    
    if v24 == None:
        v24=' '    
    if v25 == None:
        v25=' '    
    if v26 == None:
        v26=' '    
    if v27 == None:
        v27=' '    
    if v28 == None:
        v28=' '    
    if v29 == None:
        v29=' '    
    if v30 == None:
        v30=' '    
    if v31 == None:
        v31=' '    
    if v32 == None:
        v32=' '    
    if v33 == None:
        v33=' '    
    if v34 == None:
        v34=' '    
    if v35 == None:
        v35=' '    
    if v36 == None:
        v36=' '
    if v37 == None:
        v37=' '
    if v38 == None:
        v38=' '
    if v39 == None:
        v39=' '
    if v40 == None:
        v40=' '
    if v41 == None:
        v41=' '
    if v42 == None:
        v42=' '
    if v43 == None:
        v43=' '
    if v44 == None:
        v44=' '
    if v45 == None:
        v45=' '
    if v46 == None:
        v46=' '
    if v47 == None:
        v47=' '
    if v48 == None:
        v48=' '
    if v49 == None:
        v49=' '
    if v50 == None:
        v50=' '
    if v51 == None:
        v51=' '
    if v52 == None:
        v52=' '
    if v53 == None:
        v53=' '
    if v54 == None:
        v54=' '
    if v55 == None:
        v55=' '
    if v56 == None:
        v56=' '
    if v57 == None:
        v57=' '
    if v58 == None:
        v58=' '
    if v59 == None:
        v59=' '
    if v60 == None:
        v60=' '
    if v61 == None:
        v61=' '
    if v62 == None:
        v62=' '
    if v63 == None:
        v63=' '
    if v64 == None:
        v64=' '
    if v65 == None:
        v65=' '
    if v66 == None:
        v66=' '
    if v67 == None:
        v67=' '
    if v68 == None:
        v68=' '
    if v69 == None:
        v69=' '
    if v70 == None:
        v70=' '
    if v71 == None:
        v71=' '
    if v72 == None:
        v72=' '
    if v73 == None:
        v73=' '
    if v74 == None:
        v74=' '
    if v75 == None:
        v75=' '
    if v76 == None:
        v76=' '
    if v77 == None:
        v77=' '
    if v78 == None:
        v78=' '
    if v79 == None:
        v79=' '
    if v80 == None:
        v80=' '
    if v81 == None:
        v81=' '
    if v82 == None:
        v82=' '
    if v83 == None:
        v83=' '
    if v84 == None:
        v84=' '
    if v85 == None:
        v85=' '
    if x8 == None:
        x8= ' '
    if x9 == None:
        x9= ' '
    if x10 == None:
        x10= ' '
    if x11 == None:
        x11= ' '
    if x12 == None:
        x12= ' '
    if x13 == None:
        x13= ' '
    if x14 == None:
        x14= ' '
    if x15 == None:
        x15= ' '
    if x16 == None:
        x16= ' '
    if x17 == None:
        x17= ' '
    if x18 == None:
        x18= ' '
    if x19 == None:
        x19= ' '
    if x21 == None:
        x21=' '    
    if x22 == None:
        x22=' '    
    if x23 == None:
        x23=' '    
    if x24 == None:
        x24=' '    
    if x25 == None:
        x25=' '    
    if x26 == None:
        x26=' '    
    if x27 == None:
        x27=' '    
    if x28 == None:
        x28=' '    
    if x29 == None:
        x29=' '    
    if x30 == None:
        x30=' '    
    if x31 == None:
        x31=' '    
    if x32 == None:
        x32=' '    
    if x33 == None:
        x33=' '    
    if x34 == None:
        x34=' '    
    if x35 == None:
        x35=' '    
    if x36 == None:
        x36=' '
    if x37 == None:
        x37=' '
    if x38 == None:
        x38=' '
    if x39 == None:
        x39=' '
    if x40 == None:
        x40=' '
    if x41 == None:
        x41=' '
    if x42 == None:
        x42=' '
    if x43 == None:
        x43=' '
    if x44 == None:
        x44=' '
    if x45 == None:
        x45=' '
    if x46 == None:
        x46=' '
    if x47 == None:
        x47=' '
    if x48 == None:
        x48=' '
    if x49 == None:
        x49=' '
    if x50 == None:
        x50=' '
    if x51 == None:
        x51=' '
    if x52 == None:
        x52=' '
    if x53 == None:
        x53=' '
    if x54 == None:
        x54=' '
    if x55 == None:
        x55=' '
    if x56 == None:
        x56=' '
    if x57 == None:
        x57=' '
    if x58 == None:
        x58=' '
    if x59 == None:
        x59=' '
    if x60 == None:
        x60=' '
    if x61 == None:
        x61=' '
    if x62 == None:
        x62=' '
    if x63 == None:
        x63=' '
    if x64 == None:
        x64=' '
    if x65 == None:
        x65=' '
    if x66 == None:
        x66=' '
    if x67 == None:
        x67=' '
    if x68 == None:
        x68=' '
    if x69 == None:
        x69=' '
    if x70 == None:
        x70=' '
    if x71 == None:
        x71=' '
    if x72 == None:
        x72=' '
    if x73 == None:
        x73=' '
    if x74 == None:
        x74=' '
    if x75 == None:
        x75=' '
    if x76 == None:
        x76=' '
    if x77 == None:
        x77=' '
    if x78 == None:
        x78=' '
    if x79 == None:
        x79=' '
    if x80 == None:
        x80=' '
    if x81 == None:
        x81=' '
    if x82 == None:
        x82=' '
    if x83 == None:
        x83=' '
    if x84 == None:
        x84=' '
    if x85 == None:
        x85=' '
    #если пара больше 40 символов
    a='qwertyuioplkjhgfdsazxcvbnmkjhgfdrtyuiojg'
    if len(v8) > len(a):
        v8= v8[:-30]
    if len(v9) > len(a):
        v9= v9[:-30]
    if len(v10) > len(a):
        v10= v10[:-30]
    if len(v11) > len(a):
        v11= v11[:-30]
    if len(v12) > len(a):
        v12= v12[:-30]
    if len(v13) > len(a):
        v13= v13[:-30]
    if len(v14) > len(a):
        v14= v14[:-30]
    if len(v15) > len(a):
        v15= v15[:-30]
    if len(v16) > len(a):
        v16= v16[:-30]
    if len(v17) > len(a):
        v17= v17[:-30]
    if len(v18) > len(a):
        v18= v18[:-30]
    if len(v19) > len(a):
        v19= v19[:-30]
    if len(v21) > len(a):
        v21= v21[:-30]
    if len(v22) > len(a):
        v22= v22[:-30]
    if len(v23) > len(a):
        v23= v23[:-30]
    if len(v24) > len(a):
        v24= v24[:-30]
    if len(v25) > len(a):
        v25= v25[:-30]
    if len(v26) > len(a):
        v26= v26[:-30]
    if len(v27) > len(a):
        v27= v27[:-30]
    if len(v28) > len(a):
        v28= v28[:-30]
    if len(v29) > len(a):
        v29= v29[:-30]
    if len(v30) > len(a):
        v30= v30[:-30]
    if len(v31) > len(a):
        v31= v31[:-30]
    if len(v32) > len(a):
        v32= v32[:-30]
    if len(v33) > len(a):
        v33= v33[:-30]
    if len(v34) > len(a):
        v34= v34[:-30]
    if len(v35) > len(a):
        v35= v35[:-30]
    if len(v36) > len(a):
        v36= v36[:-30]
    if len(v37) > len(a):
        v37= v37[:-30]
    if len(v38) > len(a):
        v38= v38[:-30]
    if len(v39) > len(a):
        v39= v39[:-30]
    if len(v40) > len(a):
        v40= v40[:-30]
    if len(v41) > len(a):
        v41= v41[:-30]
    if len(v42) > len(a):
        v42= v42[:-30]
    if len(v43) > len(a):
        v43= v43[:-30]
    if len(v44) > len(a):
        v44= v44[:-30]
    if len(v45) > len(a):
        v45= v45[:-30]
    if len(v46) > len(a):
        v46= v46[:-30]
    if len(v47) > len(a):
        v47= v47[:-30]
    if len(v48) > len(a):
        v48= v48[:-30]
    if len(v49) > len(a):
        v49= v49[:-30]
    if len(v50) > len(a):
        v50= v50[:-30]
    if len(v51) > len(a):
        v51= v51[:-30]
    if len(v52) > len(a):
        v52= v52[:-30]
    if len(v53) > len(a):
        v53= v53[:-30]
    if len(v54) > len(a):
        v54= v54[:-30]
    if len(v55) > len(a):
        v55= v55[:-30]
    if len(v56) > len(a):
        v56= v56[:-30]
    if len(v57) > len(a):
        v57= v57[:-30]
    if len(v58) > len(a):
        v58= v58[:-30]
    if len(v59) > len(a):
        v59= v59[:-30]
    if len(v60) > len(a):
        v60= v60[:-30]
    if len(v61) > len(a):
        v61= v61[:-30]
    if len(v62) > len(a):
        v62= v62[:-30]
    if len(v63) > len(a):
        v63= v63[:-30]
    if len(v64) > len(a):
        v64= v64[:-30]
    if len(v65) > len(a):
        v65= v65[:-30]
    if len(v66) > len(a):
        v66= v66[:-30]
    if len(v67) > len(a):
        v67= v67[:-30]
    if len(v68) > len(a):
        v68= v68[:-30]
    if len(v69) > len(a):
        v69= v69[:-30]
    if len(v70) > len(a):
        v70= v70[:-30]
    if len(v71) > len(a):
        v71= v71[:-30]
    if len(v72) > len(a):
        v72= v72[:-30]
    if len(v73) > len(a):
        v73= v73[:-30]
    if len(v74) > len(a):
        v74= v74[:-30]
    if len(v75) > len(a):
        v75= v75[:-30]
    if len(v76) > len(a):
        v76= v76[:-30]
    if len(v77) > len(a):
        v77= v77[:-30]
    if len(v78) > len(a):
        v78= v78[:-30]
    if len(v79) > len(a):
        v79= v79[:-30]
    if len(v80) > len(a):
        v80= v80[:-30]
    if len(v81) > len(a):
        v81= v81[:-30]
    if len(v82) > len(a):
        v82= v82[:-30]
    if len(v83) > len(a):
        v83= v83[:-30]
    if len(v84) > len(a):
        v84= v84[:-30]
    if len(v85) > len(a):
        v85= v85[:-30]

    branch.set(path_sample,font_sample,40,740,120,x8,image_output)
    branch.set(image_output,font_sample,40,740,200,x10,image_output)
    branch.set(image_output,font_sample,40,740,280,x12,image_output)
    branch.set(image_output,font_sample,40,740,360,x14,image_output)
    branch.set(image_output,font_sample,40,740,440,x16,image_output)
    branch.set(image_output,font_sample,40,740,520,x18,image_output)
    branch.set(image_output,font_sample,40,1740,120,x21,image_output)
    branch.set(image_output,font_sample,40,1740,200,x23,image_output)
    branch.set(image_output,font_sample,40,1740,280,x25,image_output)
    branch.set(image_output,font_sample,40,1740,360,x27,image_output)
    branch.set(image_output,font_sample,40,1740,440,x29,image_output)
    branch.set(image_output,font_sample,40,1740,520,x31,image_output)
    branch.set(image_output,font_sample,40,2740,120,x35,image_output)
    branch.set(image_output,font_sample,40,2740,200,x37,image_output)
    branch.set(image_output,font_sample,40,2740,280,x39,image_output)
    branch.set(image_output,font_sample,40,2740,360,x41,image_output)
    branch.set(image_output,font_sample,40,2740,440,x43,image_output)
    branch.set(image_output,font_sample,40,2740,520,x45,image_output)
    branch.set(image_output,font_sample,40,740,1060,x48,image_output)
    branch.set(image_output,font_sample,40,740,1140,x50,image_output)
    branch.set(image_output,font_sample,40,740,1240,x52,image_output)
    branch.set(image_output,font_sample,40,740,1320,x54,image_output)
    branch.set(image_output,font_sample,40,740,1400,x56,image_output)
    branch.set(image_output,font_sample,40,740,1480,x58,image_output)
    branch.set(image_output,font_sample,40,1740,1060,x61,image_output)
    branch.set(image_output,font_sample,40,1740,1140,x63,image_output)
    branch.set(image_output,font_sample,40,1740,1240,x65,image_output)
    branch.set(image_output,font_sample,40,1740,1320,x67,image_output)
    branch.set(image_output,font_sample,40,1740,1400,x69,image_output)
    branch.set(image_output,font_sample,40,1740,1480,x71,image_output)
    branch.set(image_output,font_sample,40,2740,1060,x74,image_output)
    branch.set(image_output,font_sample,40,2740,1140,x76,image_output)
    branch.set(image_output,font_sample,40,2740,1240,x78,image_output)
    branch.set(image_output,font_sample,40,2740,1320,x80,image_output)
    branch.set(image_output,font_sample,40,2740,1400,x82,image_output)
    branch.set(image_output,font_sample,40,2740,1480,x84,image_output)
    branch.set(image_output,font_sample,40,60,120,v8,image_output)
    branch.set(image_output,font_sample,30,60,160,v9,image_output)
    branch.set(image_output,font_sample,40,60,200,v10,image_output)
    branch.set(image_output,font_sample,30,60,240,v11,image_output)
    branch.set(image_output,font_sample,40,60,280,x16,image_output)
    branch.set(image_output,font_sample,30,60,320,v13,image_output)
    branch.set(image_output,font_sample,40,60,360,v14,image_output)
    branch.set(image_output,font_sample,30,60,400,v15,image_output)
    branch.set(image_output,font_sample,40,60,440,v16,image_output)
    branch.set(image_output,font_sample,30,60,480,v17,image_output)
    branch.set(image_output,font_sample,40,60,520,v18,image_output)
    branch.set(image_output,font_sample,30,60,560,v19,image_output)
    branch.set(image_output,font_sample,40,1060,120,v21,image_output)
    branch.set(image_output,font_sample,30,1060,160,v22,image_output)
    branch.set(image_output,font_sample,40,1060,200,v23,image_output)
    branch.set(image_output,font_sample,30,1060,240,v24,image_output)
    branch.set(image_output,font_sample,40,1060,280,v25,image_output)
    branch.set(image_output,font_sample,30,1060,320,v26,image_output)
    branch.set(image_output,font_sample,40,1060,360,v27,image_output)
    branch.set(image_output,font_sample,30,1060,400,v28,image_output)
    branch.set(image_output,font_sample,40,1060,440,v29,image_output)
    branch.set(image_output,font_sample,30,1060,480,v30,image_output)
    branch.set(image_output,font_sample,40,1060,520,v31,image_output)
    branch.set(image_output,font_sample,30,1060,560,v32,image_output)
    branch.set(image_output,font_sample,40,2060,120,v35,image_output)
    branch.set(image_output,font_sample,30,2060,160,v36,image_output)
    branch.set(image_output,font_sample,40,2060,200,v37,image_output)
    branch.set(image_output,font_sample,30,2060,240,v38,image_output)
    branch.set(image_output,font_sample,40,2060,280,v39,image_output)
    branch.set(image_output,font_sample,30,2060,320,v40,image_output)
    branch.set(image_output,font_sample,40,2060,360,v41,image_output)
    branch.set(image_output,font_sample,30,2060,400,v42,image_output)
    branch.set(image_output,font_sample,40,2060,440,v43,image_output)
    branch.set(image_output,font_sample,30,2060,480,v44,image_output)
    branch.set(image_output,font_sample,40,2060,520,v45,image_output)
    branch.set(image_output,font_sample,30,2060,560,v46,image_output)
    branch.set(image_output,font_sample,40,60,1060,v48,image_output)
    branch.set(image_output,font_sample,30,60,1100,v49,image_output)
    branch.set(image_output,font_sample,40,60,1140,v50,image_output)
    branch.set(image_output,font_sample,30,60,1180,v51,image_output)
    branch.set(image_output,font_sample,40,60,1220,v52,image_output)
    branch.set(image_output,font_sample,30,60,1260,v53,image_output)
    branch.set(image_output,font_sample,40,60,1300,v54,image_output)
    branch.set(image_output,font_sample,30,60,1340,v55,image_output)
    branch.set(image_output,font_sample,40,60,1380,v56,image_output)
    branch.set(image_output,font_sample,30,60,1420,v57,image_output)
    branch.set(image_output,font_sample,40,60,1460,v58,image_output)
    branch.set(image_output,font_sample,30,60,1500,v59,image_output)
    branch.set(image_output,font_sample,40,1060,1060,v61,image_output)
    branch.set(image_output,font_sample,30,1060,1100,v62,image_output)
    branch.set(image_output,font_sample,40,1060,1140,v63,image_output)
    branch.set(image_output,font_sample,30,1060,1180,v64,image_output)
    branch.set(image_output,font_sample,40,1060,1220,v65,image_output)
    branch.set(image_output,font_sample,30,1060,1260,v66,image_output)
    branch.set(image_output,font_sample,40,1060,1300,v67,image_output)
    branch.set(image_output,font_sample,30,1060,1340,v68,image_output)
    branch.set(image_output,font_sample,40,1060,1380,v69,image_output)
    branch.set(image_output,font_sample,30,1060,1420,v70,image_output)
    branch.set(image_output,font_sample,40,1060,1460,v71,image_output)
    branch.set(image_output,font_sample,30,1060,1500,v72,image_output)
    branch.set(image_output,font_sample,40,2060,1060,v74,image_output)
    branch.set(image_output,font_sample,30,2060,1100,v75,image_output)
    branch.set(image_output,font_sample,40,2060,1140,v76,image_output)
    branch.set(image_output,font_sample,30,2060,1180,v77,image_output)
    branch.set(image_output,font_sample,40,2060,1220,v78,image_output)
    branch.set(image_output,font_sample,30,2060,1260,v79,image_output)
    branch.set(image_output,font_sample,40,2060,1300,v80,image_output)
    branch.set(image_output,font_sample,30,2060,1340,v81,image_output)
    branch.set(image_output,font_sample,40,2060,1380,v82,image_output)
    branch.set(image_output,font_sample,30,2060,1420,v83,image_output)
    branch.set(image_output,font_sample,40,2060,1460,v84,image_output)
    branch.set(image_output,font_sample,30,2060,1500,v85,image_output)

#---Производительность-------------------------------#
    branch.center_bar()                              #
    res = "%s СЕК" % (time.time() - start_time)      #
    im = Image.open(image_output)                    #
    font = ImageFont.truetype(font_sample, size=30)  #
    draw_text = ImageDraw.Draw(im)                   #
    draw_text.text(                                  #
    (1168, 794),                                     #
    str(res),                                        #
    font=font,                                       #
    fill='#3A4046')                                  #
    im.save(image_output)                            #
#----------------------------------------------------#
