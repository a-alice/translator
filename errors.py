from enum import Enum

class ErrorCode(Enum):
    no_error = 0
    type_error = 1
    name_f_error = 2
    name_p_error =3
    params_error = 4
    end_error = 5

errors = {ErrorCode.no_error: 'good func',
          ErrorCode.type_error: 'Error in type name',
          ErrorCode.name_f_error: 'Error in func name',
          ErrorCode.name_p_error: 'Error in param name',
          ErrorCode.params_error: 'Error in params syntax',
          ErrorCode.end_error: 'Error finish func'}
