# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyscada', '0022_auto_20160228_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMbusDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_type', models.CharField(max_length=400, choices=[('ups_pico', 'UPS PIco')])),
                ('port', models.CharField(default='1', max_length=400)),
                ('address', models.PositiveSmallIntegerField(default=None, null=True, choices=[(0, '0x0x0/0'), (1, '0x0x1/1'), (2, '0x0x2/2'), (3, '0x0x3/3'), (4, '0x0x4/4'), (5, '0x0x5/5'), (6, '0x0x6/6'), (7, '0x0x7/7'), (8, '0x0x8/8'), (9, '0x0x9/9'), (10, '0x0xa/10'), (11, '0x0xb/11'), (12, '0x0xc/12'), (13, '0x0xd/13'), (14, '0x0xe/14'), (15, '0x0xf/15'), (16, '0x0x10/16'), (17, '0x0x11/17'), (18, '0x0x12/18'), (19, '0x0x13/19'), (20, '0x0x14/20'), (21, '0x0x15/21'), (22, '0x0x16/22'), (23, '0x0x17/23'), (24, '0x0x18/24'), (25, '0x0x19/25'), (26, '0x0x1a/26'), (27, '0x0x1b/27'), (28, '0x0x1c/28'), (29, '0x0x1d/29'), (30, '0x0x1e/30'), (31, '0x0x1f/31'), (32, '0x0x20/32'), (33, '0x0x21/33'), (34, '0x0x22/34'), (35, '0x0x23/35'), (36, '0x0x24/36'), (37, '0x0x25/37'), (38, '0x0x26/38'), (39, '0x0x27/39'), (40, '0x0x28/40'), (41, '0x0x29/41'), (42, '0x0x2a/42'), (43, '0x0x2b/43'), (44, '0x0x2c/44'), (45, '0x0x2d/45'), (46, '0x0x2e/46'), (47, '0x0x2f/47'), (48, '0x0x30/48'), (49, '0x0x31/49'), (50, '0x0x32/50'), (51, '0x0x33/51'), (52, '0x0x34/52'), (53, '0x0x35/53'), (54, '0x0x36/54'), (55, '0x0x37/55'), (56, '0x0x38/56'), (57, '0x0x39/57'), (58, '0x0x3a/58'), (59, '0x0x3b/59'), (60, '0x0x3c/60'), (61, '0x0x3d/61'), (62, '0x0x3e/62'), (63, '0x0x3f/63'), (64, '0x0x40/64'), (65, '0x0x41/65'), (66, '0x0x42/66'), (67, '0x0x43/67'), (68, '0x0x44/68'), (69, '0x0x45/69'), (70, '0x0x46/70'), (71, '0x0x47/71'), (72, '0x0x48/72'), (73, '0x0x49/73'), (74, '0x0x4a/74'), (75, '0x0x4b/75'), (76, '0x0x4c/76'), (77, '0x0x4d/77'), (78, '0x0x4e/78'), (79, '0x0x4f/79'), (80, '0x0x50/80'), (81, '0x0x51/81'), (82, '0x0x52/82'), (83, '0x0x53/83'), (84, '0x0x54/84'), (85, '0x0x55/85'), (86, '0x0x56/86'), (87, '0x0x57/87'), (88, '0x0x58/88'), (89, '0x0x59/89'), (90, '0x0x5a/90'), (91, '0x0x5b/91'), (92, '0x0x5c/92'), (93, '0x0x5d/93'), (94, '0x0x5e/94'), (95, '0x0x5f/95'), (96, '0x0x60/96'), (97, '0x0x61/97'), (98, '0x0x62/98'), (99, '0x0x63/99'), (100, '0x0x64/100'), (101, '0x0x65/101'), (102, '0x0x66/102'), (103, '0x0x67/103'), (104, '0x0x68/104'), (105, '0x0x69/105'), (106, '0x0x6a/106'), (107, '0x0x6b/107'), (108, '0x0x6c/108'), (109, '0x0x6d/109'), (110, '0x0x6e/110'), (111, '0x0x6f/111'), (112, '0x0x70/112'), (113, '0x0x71/113'), (114, '0x0x72/114'), (115, '0x0x73/115'), (116, '0x0x74/116'), (117, '0x0x75/117'), (118, '0x0x76/118'), (119, '0x0x77/119'), (120, '0x0x78/120'), (121, '0x0x79/121'), (122, '0x0x7a/122'), (123, '0x0x7b/123'), (124, '0x0x7c/124'), (125, '0x0x7d/125'), (126, '0x0x7e/126'), (127, '0x0x7f/127'), (128, '0x0x80/128'), (129, '0x0x81/129'), (130, '0x0x82/130'), (131, '0x0x83/131'), (132, '0x0x84/132'), (133, '0x0x85/133'), (134, '0x0x86/134'), (135, '0x0x87/135'), (136, '0x0x88/136'), (137, '0x0x89/137'), (138, '0x0x8a/138'), (139, '0x0x8b/139'), (140, '0x0x8c/140'), (141, '0x0x8d/141'), (142, '0x0x8e/142'), (143, '0x0x8f/143'), (144, '0x0x90/144'), (145, '0x0x91/145'), (146, '0x0x92/146'), (147, '0x0x93/147'), (148, '0x0x94/148'), (149, '0x0x95/149'), (150, '0x0x96/150'), (151, '0x0x97/151'), (152, '0x0x98/152'), (153, '0x0x99/153'), (154, '0x0x9a/154'), (155, '0x0x9b/155'), (156, '0x0x9c/156'), (157, '0x0x9d/157'), (158, '0x0x9e/158'), (159, '0x0x9f/159'), (160, '0x0xa0/160'), (161, '0x0xa1/161'), (162, '0x0xa2/162'), (163, '0x0xa3/163'), (164, '0x0xa4/164'), (165, '0x0xa5/165'), (166, '0x0xa6/166'), (167, '0x0xa7/167'), (168, '0x0xa8/168'), (169, '0x0xa9/169'), (170, '0x0xaa/170'), (171, '0x0xab/171'), (172, '0x0xac/172'), (173, '0x0xad/173'), (174, '0x0xae/174'), (175, '0x0xaf/175'), (176, '0x0xb0/176'), (177, '0x0xb1/177'), (178, '0x0xb2/178'), (179, '0x0xb3/179'), (180, '0x0xb4/180'), (181, '0x0xb5/181'), (182, '0x0xb6/182'), (183, '0x0xb7/183'), (184, '0x0xb8/184'), (185, '0x0xb9/185'), (186, '0x0xba/186'), (187, '0x0xbb/187'), (188, '0x0xbc/188'), (189, '0x0xbd/189'), (190, '0x0xbe/190'), (191, '0x0xbf/191'), (192, '0x0xc0/192'), (193, '0x0xc1/193'), (194, '0x0xc2/194'), (195, '0x0xc3/195'), (196, '0x0xc4/196'), (197, '0x0xc5/197'), (198, '0x0xc6/198'), (199, '0x0xc7/199'), (200, '0x0xc8/200'), (201, '0x0xc9/201'), (202, '0x0xca/202'), (203, '0x0xcb/203'), (204, '0x0xcc/204'), (205, '0x0xcd/205'), (206, '0x0xce/206'), (207, '0x0xcf/207'), (208, '0x0xd0/208'), (209, '0x0xd1/209'), (210, '0x0xd2/210'), (211, '0x0xd3/211'), (212, '0x0xd4/212'), (213, '0x0xd5/213'), (214, '0x0xd6/214'), (215, '0x0xd7/215'), (216, '0x0xd8/216'), (217, '0x0xd9/217'), (218, '0x0xda/218'), (219, '0x0xdb/219'), (220, '0x0xdc/220'), (221, '0x0xdd/221'), (222, '0x0xde/222'), (223, '0x0xdf/223'), (224, '0x0xe0/224'), (225, '0x0xe1/225'), (226, '0x0xe2/226'), (227, '0x0xe3/227'), (228, '0x0xe4/228'), (229, '0x0xe5/229'), (230, '0x0xe6/230'), (231, '0x0xe7/231'), (232, '0x0xe8/232'), (233, '0x0xe9/233'), (234, '0x0xea/234'), (235, '0x0xeb/235'), (236, '0x0xec/236'), (237, '0x0xed/237'), (238, '0x0xee/238'), (239, '0x0xef/239'), (240, '0x0xf0/240'), (241, '0x0xf1/241'), (242, '0x0xf2/242'), (243, '0x0xf3/243'), (244, '0x0xf4/244'), (245, '0x0xf5/245'), (246, '0x0xf6/246'), (247, '0x0xf7/247'), (248, '0x0xf8/248'), (249, '0x0xf9/249'), (250, '0x0xfa/250'), (251, '0x0xfb/251'), (252, '0x0xfc/252'), (253, '0x0xfd/253'), (254, '0x0xfe/254'), (255, '0x0xff/255')])),
                ('smbus_device', models.OneToOneField(to='pyscada.Device', on_delete=models.SET_NULL)),
            ],
        ),
        migrations.CreateModel(
            name='SMbusVariable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('information', models.CharField(default='None', max_length=400)),
                ('smbus_variable', models.OneToOneField(to='pyscada.Variable', on_delete=models.SET_NULL)),
            ],
        ),
    ]
