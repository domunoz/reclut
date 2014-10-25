# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
            ],
            options={
                'ordering': ('nombre',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Medio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Postulante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(null=True, verbose_name=b'entrevista', blank=True)),
                ('rut', models.CharField(max_length=140, null=True, blank=True)),
                ('nombres', models.CharField(max_length=140)),
                ('apellidos', models.CharField(max_length=140)),
                ('domicilio', models.CharField(max_length=140, null=True, blank=True)),
                ('comuna', models.CharField(max_length=140, null=True, blank=True)),
                ('comuna2', models.CharField(blank=True, max_length=5, null=True, choices=[(b'15101', 'Arica'), (b'15102', 'Camarones'), (b'15201', 'Putre'), (b'15202', 'General '), (b'01101', 'Iquique'), (b'01107', 'Alto Hospicio'), (b'01401', 'Pozo Almonte'), (b'01402', 'Cami\xf1a'), (b'01403', 'Colchane'), (b'01404', 'Huara'), (b'01405', 'Pica'), (b'02101', 'Antofagasta'), (b'02102', 'Mejillones'), (b'02103', 'Sierra Gorda'), (b'02104', 'Taltal'), (b'02201', 'Calama'), (b'02202', 'Ollag\xfce'), (b'02203', 'San Pedro de Atacama'), (b'02301', 'Tocopilla'), (b'02302', 'Mar\xeda Elena'), (b'03101', 'Copiap\xf3'), (b'03102', 'Caldera'), (b'03103', 'Tierra Amarilla'), (b'03201', 'Cha\xf1aral'), (b'03202', 'Diego de Almagro'), (b'03301', 'Vallenar'), (b'03302', 'Alto del Carmen'), (b'03303', 'Freirina'), (b'03304', 'Huasco'), (b'04101', 'La Serena'), (b'04102', 'Coquimbo'), (b'04103', 'Andacollo'), (b'04104', 'La Higuera'), (b'04105', 'Paiguano'), (b'04106', 'Vicu\xf1a'), (b'04201', 'Illapel'), (b'04202', 'Canela'), (b'04203', 'Los Vilos'), (b'04204', 'Salamanca'), (b'04301', 'Ovalle'), (b'04302', 'Combarbal\xe1'), (b'04303', 'Monte Patria'), (b'04304', 'Punitaqui'), (b'04305', 'R\xedo Hurtado'), (b'05101', 'Valpara\xedso'), (b'05102', 'Casablanca'), (b'05103', 'Conc\xf3n'), (b'05104', 'Juan Fern\xe1ndez'), (b'05105', 'Puchuncav\xed'), (b'05107', 'Quintero'), (b'05109', 'Vi\xf1a del Mar'), (b'05201', 'Isla de Pascua'), (b'05301', 'Los Andes'), (b'05302', 'Calle Larga'), (b'05303', 'Rinconada'), (b'05304', 'San Esteban'), (b'05401', 'La Ligua'), (b'05402', 'Cabildo'), (b'05403', 'Papudo'), (b'05404', 'Petorca'), (b'05405', 'Zapallar'), (b'05501', 'Quillota'), (b'05502', 'Calera'), (b'05503', 'Hijuelas'), (b'05504', 'La Cruz'), (b'05506', 'Nogales'), (b'05601', 'San Antonio'), (b'05602', 'Algarrobo'), (b'05603', 'Cartagena'), (b'05604', 'El Quisco'), (b'05605', 'El Tabo'), (b'05606', 'Santo Domingo'), (b'05701', 'San Felipe'), (b'05702', 'Catemu'), (b'05703', 'Llaillay'), (b'05704', 'Panquehue'), (b'05705', 'Putaendo'), (b'05706', 'Santa Mar\xeda'), (b'05801', 'Quilpu\xe9'), (b'05801', 'Limache'), (b'05801', 'Olmu\xe9'), (b'05801', 'Villa Alemana'), (b'06101', 'Rancagua'), (b'06102', 'Codegua'), (b'06103', 'Coinco'), (b'06104', 'Coltauco'), (b'06105', 'Do\xf1ihue'), (b'06106', 'Graneros'), (b'06107', 'Las Cabras'), (b'06108', 'Machal\xed'), (b'06109', 'Malloa'), (b'06110', 'Mostazal'), (b'06111', 'Olivar'), (b'06112', 'Peumo'), (b'06113', 'Pichidegua'), (b'06114', 'Quinta de Tilcoco'), (b'06115', 'Rengo'), (b'06116', 'Requ\xednoa'), (b'06117', 'San Vicente'), (b'06201', 'Pichilemu'), (b'06202', 'La Estrella'), (b'06203', 'Litueche'), (b'06204', 'Marchihue'), (b'06205', 'Navidad'), (b'06206', 'Paredones'), (b'06301', 'San Fernando'), (b'06302', 'Ch\xe9pica'), (b'06303', 'Chimbarongo'), (b'06304', 'Lolol'), (b'06305', 'Nancagua'), (b'06306', 'Palmilla'), (b'06307', 'Peralillo'), (b'06308', 'Placilla'), (b'06309', 'Pumanque'), (b'06310', 'Santa Cruz'), (b'07101', 'Talca'), (b'07102', 'Constituci\xf3n'), (b'07103', 'Curepto'), (b'07104', 'Empedrado'), (b'07105', 'Maule'), (b'07106', 'Pelarco'), (b'07107', 'Pencahue'), (b'07108', 'R\xedo Claro'), (b'07109', 'San Clemente'), (b'07110', 'San Rafael'), (b'07201', 'Cauquenes'), (b'07202', 'Chanco'), (b'07203', 'Pelluhue'), (b'07301', 'Curic\xf3'), (b'07302', 'Huala\xf1e'), (b'07303', 'Licant\xe9n'), (b'07304', 'Molina'), (b'07305', 'Rauco'), (b'07306', 'Romeral'), (b'07307', 'Sagrada Familia'), (b'07308', 'Teno'), (b'07309', 'Vichuqu\xe9n'), (b'07401', 'Linares'), (b'07402', 'Colb\xfan'), (b'07403', 'Longav\xed'), (b'07404', 'Parral'), (b'07405', 'Retiro'), (b'07406', 'San Javier'), (b'07407', 'Villa Alegre'), (b'07408', 'Yerbas Buenas'), (b'08101', 'Concepci\xf3n'), (b'08102', 'Coronel'), (b'08103', 'Chiguayante'), (b'08104', 'Florida'), (b'08105', 'Hualqui'), (b'08106', 'Lota'), (b'08107', 'Penco'), (b'08108', 'San Pedro de la Paz'), (b'08109', 'Santa Juana'), (b'08110', 'Talcahuano'), (b'08111', 'Tompe'), (b'08112', 'Hualp\xe9n'), (b'08201', 'Lebu'), (b'08202', 'Arauco'), (b'08203', 'Ca\xf1eete'), (b'08204', 'Contulmo'), (b'08205', 'Curanilahue'), (b'08206', 'Los Alamos'), (b'08207', 'Tir\xfaa'), (b'08301', 'Los Angeles'), (b'08302', 'Antuco'), (b'08303', 'Cabrero'), (b'08304', 'Laja'), (b'08305', 'Mulch\xe9n'), (b'08306', 'Nacimiento'), (b'08307', 'Negrete'), (b'08308', 'Quilaco'), (b'08309', 'Quilleco'), (b'08310', 'San Rosendo'), (b'08311', 'Santa B\xe1rbara'), (b'08312', 'Tucapel'), (b'08313', 'Yumbel'), (b'08314', 'Alto Biob\xedo'), (b'08401', 'Chill\xe1n'), (b'08402', 'Bulnes'), (b'08403', 'Cobquecura'), (b'08404', 'Coelemu'), (b'08405', 'Coihueco'), (b'08406', 'Chill\xe1n Viejo'), (b'08407', 'El Carmen'), (b'08408', 'Ninhue'), (b'08409', '\xd1iqu\xe9n'), (b'08410', 'Pemuco'), (b'08411', 'Pinto'), (b'08412', 'Portezuelo'), (b'08413', 'Quill\xf3n'), (b'08414', 'Quirihue'), (b'08415', 'R\xe1uil'), (b'08416', 'San Carlos'), (b'08417', 'San Fabi\xe1n'), (b'08418', 'San Ignacio'), (b'08419', 'San Nicol\xe1s'), (b'08420', 'Treguaco'), (b'08421', 'Yungay'), (b'09101', 'Temuco'), (b'09102', 'Carahue'), (b'09103', 'Cunco'), (b'09104', 'Curarrehue'), (b'09105', 'Freire'), (b'09106', 'Galvarino'), (b'09107', 'Gorbea'), (b'09108', 'Lautaro'), (b'09109', 'Loncoche'), (b'09110', 'Melipeuco'), (b'09111', 'Nueva Imperial'), (b'09112', 'Padre Las Casas'), (b'09113', 'Perquenco'), (b'09114', 'Pitrufqu\xe9n'), (b'09115', 'Puc\xf3n'), (b'09116', 'Saavedra'), (b'09117', 'Teodoro Schmidt'), (b'09118', 'Tolt\xe9n'), (b'09119', 'Vilc\xfan'), (b'09120', 'Villarrica'), (b'09121', 'Cholchol'), (b'09201', 'Angol'), (b'09202', 'Collipulli'), (b'09203', 'Curacaut\xedn'), (b'09204', 'Ercilla'), (b'09205', 'Lonquimay'), (b'09206', 'Los Sauces'), (b'09207', 'Lumaco'), (b'09208', 'Pur\xe9n'), (b'09209', 'Renaico'), (b'09210', 'Traigu\xe9n'), (b'09211', 'Victoria'), (b'14101', 'Valdivia'), (b'14102', 'Corral'), (b'14103', 'Lanco'), (b'14104', 'Los Lagos'), (b'14105', 'M\xe1fil'), (b'14106', 'Mariquina'), (b'14107', 'Paillaco'), (b'14108', 'Panguipulli'), (b'14201', 'La Uni\xf3n'), (b'14202', 'Futrono'), (b'14203', 'Lago Ranco'), (b'14204', 'R\xedo Bueno'), (b'10101', 'Puerto Montt'), (b'10102', 'Calbuco'), (b'10103', 'Cocham\xf3'), (b'10104', 'Fresia'), (b'10105', 'Frutillar'), (b'10106', 'Los Muermos'), (b'10107', 'Llanquihue'), (b'10108', 'Maull\xedn'), (b'10109', 'Puerto Varas'), (b'10201', 'Castro'), (b'10202', 'Ancud'), (b'10203', 'Chonchi'), (b'10204', 'Curaco de V\xe9lez'), (b'10205', 'Dalcahue'), (b'10206', 'Puqueld\xf3n'), (b'10207', 'Queil\xe9n'), (b'10208', 'Quell\xf3n'), (b'10209', 'Quemchi'), (b'10210', 'Quinchao'), (b'10301', 'Osorno'), (b'10302', 'Puerto Octay'), (b'10303', 'Purranque'), (b'10304', 'Puyehue'), (b'10305', 'R\xedo Negro'), (b'10306', 'San Juan de la Costa'), (b'10307', 'San Pablo'), (b'10401', 'Chait\xe9n'), (b'10402', 'Futaleuf\xfa'), (b'10403', 'Hualaihu\xe9'), (b'10404', 'Palena'), (b'11101', 'Coihaique'), (b'11102', 'Lago Verde'), (b'11201', 'Ais\xe9n'), (b'11202', 'Cisnes'), (b'11203', 'Guaitecas'), (b'11301', 'Cochrane'), (b'11302', "O'Higgins"), (b'11303', 'Tortel'), (b'11401', 'Chile Chico'), (b'11402', 'R\xedo Ib\xe1\xf1ez'), (b'12101', 'Punta Arenas'), (b'12102', 'Laguna Blanca'), (b'12103', 'R\xedo Verde'), (b'12104', 'San Gregorio'), (b'12201', 'Cabo de Hornos'), (b'12202', 'Ant\xe1rtica'), (b'12301', 'Porvenir'), (b'12302', 'Primavera'), (b'12303', 'Timaukel'), (b'12401', 'Natales'), (b'12402', 'Torres del Paine'), (b'13101', 'Santiago'), (b'13102', 'Cerrillos'), (b'13103', 'Cerro Navia'), (b'13104', 'Conchal\xed'), (b'13105', 'El Bosque'), (b'13106', 'Estaci\xf3n Central'), (b'13107', 'Huechuraba'), (b'13108', 'Independencia'), (b'13109', 'La Cisterna'), (b'13110', 'La Florida'), (b'13111', 'La Granja'), (b'13112', 'La Pintana'), (b'13113', 'La Reina'), (b'13114', 'Las Condes'), (b'13115', 'Lo Barnechea'), (b'13116', 'Lo Espejo'), (b'13117', 'Lo Prado'), (b'13118', 'Macul'), (b'13119', 'Maip\xfa'), (b'13120', '\xd1u\xf1oa'), (b'13121', 'Pedro Aguirre Cerda'), (b'13122', 'Pe\xf1alol\xe9n'), (b'13123', 'Providencia'), (b'13124', 'Pudahuel'), (b'13125', 'Quilicura'), (b'13126', 'Quinta Normal'), (b'13127', 'Recoleta'), (b'13128', 'Renca'), (b'13129', 'San Joaqu\xedn'), (b'13130', 'San Miguel'), (b'13131', 'San Ram\xf3n'), (b'13132', 'Vitacura'), (b'13201', 'Puente Alto'), (b'13202', 'Pirque'), (b'13203', 'San Jos\xe9 de Maipo'), (b'13301', 'Colina'), (b'13302', 'Lampa'), (b'13303', 'Tiltil'), (b'13401', 'San Bernardo'), (b'13402', 'Buin'), (b'13403', 'Calera de Tango'), (b'13404', 'Paine'), (b'13501', 'Melipilla'), (b'13502', 'Alhu\xe9'), (b'13503', 'Curacav\xed'), (b'13504', 'Mar\xeda Pinto'), (b'13505', 'San Pedro'), (b'13601', 'Talagante'), (b'13602', 'El Monte'), (b'13603', 'Isla de Maipo'), (b'13604', 'Padre Hurtado'), (b'13605', 'Pe\xf1aflor')])),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('os10', models.BooleanField(default=False, verbose_name=b'OS-10')),
                ('sexo', models.CharField(max_length=140, null=True, blank=True)),
                ('medio', models.CharField(max_length=140, null=True, blank=True)),
                ('cargo', models.CharField(max_length=140, null=True, blank=True)),
                ('telefono', models.CharField(max_length=140, null=True, blank=True)),
                ('observaciones', models.TextField(null=True, blank=True)),
                ('contratado', models.BooleanField(default=False, verbose_name=b'contr.')),
                ('reclutador', models.CharField(max_length=140, null=True, blank=True)),
            ],
            options={
                'ordering': ('-fecha',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(to='postulantes.Region'),
            preserve_default=True,
        ),
    ]
