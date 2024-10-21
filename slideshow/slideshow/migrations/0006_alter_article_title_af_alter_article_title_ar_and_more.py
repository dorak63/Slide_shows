# Generated by Django 5.1.2 on 2024-10-20 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slideshow', '0005_alter_article_title_af_alter_article_title_ar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title_af',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_ar',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_ar_dz',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_ast',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_az',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_be',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_bg',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_bn',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_br',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_bs',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_ca',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_ckb',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_cs',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_cy',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_da',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_de',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_dsb',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_el',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_en',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_en_au',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_en_gb',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_eo',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_es',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_es_ar',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_es_co',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_es_mx',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_es_ni',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_es_ve',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_et',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_eu',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_fa',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_fi',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_fr',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_fy',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_ga',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_gd',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_gl',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_he',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_hi',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_hr',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_hsb',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_hu',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_hy',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_ia',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_id',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_ig',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_io',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_is',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_it',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_ja',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_ka',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_kab',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_kk',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_km',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_kn',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_ko',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_ky',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_lb',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_lt',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_lv',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_mk',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_ml',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_mn',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_mr',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_ms',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_my',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_nb',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_ne',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_nl',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_nn',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_os',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_pa',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_pl',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_pt',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_pt_br',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_ro',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_ru',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_sk',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_sl',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_sq',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_sr',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_sr_latn',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_sv',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_sw',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_ta',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_te',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_tg',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_th',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_tk',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_tr',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_tt',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_udm',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_ug',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_uk',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_ur',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_uz',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_vi',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_zh_hans',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_zh_hant',
            field=models.CharField(default='0', max_length=200, verbose_name='title'),
        ),
    ]
