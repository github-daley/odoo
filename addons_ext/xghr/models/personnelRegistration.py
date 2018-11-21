# -*- coding: utf-8 -*-

from odoo import models, fields, api

class personnelRegistration(models.Model):
    _name = 'personnel.registration'
    _description = 'XG HR 人员登记'
    personnel_id = fields.Many2one('personnel.group', string='所属工种')
    management_lines = fields.One2many('job.management.line', 'name')
    name = fields.Char(string='员工名称')

    street = fields.Char(string='街道')
    city = fields.Char(string='城市')
    state_id = fields.Many2one("res.country.state", string='省份', ondelete='restrict')
    zip = fields.Char(change_default=True, string='邮编')
    email = fields.Char(string='电子邮件地址')
    phone = fields.Char(string='座机电话')
    mobile = fields.Char(string='移动电话')
    image = fields.Binary(string="上传合同照片")


class personnelGroup(models.Model):
    _name = 'personnel.group'
    _description = '人员 分组'
    _rec_name = 'group_name'
    personnel_ids = fields.One2many('personnel.registration', 'personnel_id')
    group_name = fields.Char(string='工种名称')
