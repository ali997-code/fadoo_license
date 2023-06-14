# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response
import json

class FadooLicense(http.Controller):
    @http.route("/license", type="http", auth="public", methods=["post"], csrf=False)
    def license(self, **kw):
        record = request.env["fadoo_license.license"].sudo().search([])
        header_json = {"Context-Type": "application/json"}
        result = {
            "success": True,
            "status": "OK",
            "code": 200
        }
        return Response(json.dumps(result), headers=header_json)

