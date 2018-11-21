# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time

class jobManagement(models.Model):
    _name = 'job.management'
    _description = 'XG HR 工单管理 '
    _rec_name = 'uuid'

    uuid = fields.Char( string='工作单号', required=True, index=True, copy=False, default='New')  #需要方法生成
    work_describe = fields.Char(string='工作描述')
    work_type = fields.Char(string='工作种类')
    status = fields.Char(string='状态')
    prediction_time = fields.Date(string='预计工时')
    start_time = fields.Date(string='开始日期')
    Continued_time = fields.Date(string='持续时间')

    job_management_line = fields.One2many('job.management.line', 'management_line_id',string='员工')
    
    @api.model
    def create(self, vals):
        if vals.get('uuid', 'New') == 'New':
            vals['uuid'] = 'JM%s' % time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        return super(jobManagement, self).create(vals)

class  jobManagementLine(models.Model):
    _name = 'job.management.line'
    
    management_line_id = fields.Many2one('job.management', string='management_line_id')
    name = fields.Many2one('personnel.registration', string='名称', required=True)
        



