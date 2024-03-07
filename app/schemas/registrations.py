

from datetime import date
import decimal
from typing import List
# from pydantic import BaseModel
# from ..models.test_request_forms import SamplingByEnum, TestingDetail, YesOrNoEnum, ReportSentByEnum, DocumentsTypeEnum, TestingProcessEnum, DisposalProcessEnum

from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from ..models.registrations import Registration, Batch
# from .samples import TestParameterCreate

class BatchSchema(BaseModel):
    id: int
    registration_id: int
    batch_no: str
    manufactured_date: datetime
    expiry_date: datetime
    batch_size: int
    received_quantity: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: int

class TestParameterSchema(BaseModel):
    id: int
    branch_id : int
    test_type_id : int
    product_id : Optional[int]
    customer_id : Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    parameter_code : Optional[str]
    testing_parameters : Optional[str]
    amount : Optional[float]
    method_or_spec : Optional[str]
    group_of_test_parameters : str

class RegistrationTestParamsSchema(BaseModel):
    id: int
    registration_id: int
    test_params_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: int
    test_parameter : Optional[TestParameterSchema]

class RegistrationListSchema(BaseModel):
    id: int
    branch_id: int
    trf_id: int
    company_id: int
    company_name: str
    customer_address_line1: str
    customer_address_line2: str
    city: str
    state: str
    pincode_no: str
    gst: str
    date_of_registration: datetime
    date_of_received: datetime
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: int
    test_type: str
    product: int




class RegistrationSchema(BaseModel):
    id: int
    branch_id: int
    trf_id: int
    company_id: int
    company_name: str
    customer_address_line1: str
    customer_address_line2: str
    city: str
    state: str
    pincode_no: str
    gst: str
    date_of_registration: datetime
    date_of_received: datetime
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: int
    test_type: str
    product: int
    batches : Optional[list[BatchSchema]]
    test_params : Optional[list[RegistrationTestParamsSchema]]


class SampleTestParameterSchema(BaseModel):
    id: int
    sample_id: int
    test_parameter_id: int
    test_type: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: int
    test_parameter : Optional[TestParameterSchema]

class SampleSchema(BaseModel):
    id: int
    sample_id: str
    name: str
    registration_id : int
    batch_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: int
    sample_test_parameters : Optional[list[SampleTestParameterSchema]]

class SampleListSchema(BaseModel):
    id: int
    sample_id: str
    name: str
    registration_id : int
    batch_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: int
    


class SampleStatusSchema(BaseModel):
    id: int
    name: str

class SampleRequestSchema(BaseModel):
    id: int
    sample_id: int
    sample_status_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: int



class BatchCreate(BaseModel):
    batch_no: str
    manufactured_date: date
    expiry_date: date
    batch_size: int
    received_quantity: int

class RegistrationTestParamsCreate(BaseModel):
   test_params_id : int

class RegistrationCreate(BaseModel):
    branch_id: int
    trf_id: int
    company_id: int
    company_name: str
    customer_address_line1: str
    customer_address_line2: str
    city: str
    state: str
    pincode_no: str
    gst: str
    date_of_received: date
    # created_by: int
    # updated_by: int
    # created_at: datetime
    # updated_at: datetime
    test_type: str
    product: int
    batches: List[BatchCreate]
    test_params : List[RegistrationTestParamsCreate]

# class RegistrationWithBatchesCreate(BaseModel):
#     registration: RegistrationCreate
#     batches: List[BatchCreate]

class BatchUpdate(BaseModel):
    id: Optional[int]
    batch_no: Optional[str]
    manufactured_date: Optional[datetime]
    expiry_date: Optional[datetime]
    batch_size: Optional[int]
    received_quantity: Optional[int]

class RegistrationTestParamsUpdate(BaseModel):
    test_params_id: Optional[int]
    

class RegistrationUpdate(BaseModel):
    branch_id: Optional[int]
    trf_id: Optional[int]
    company_id: Optional[int]
    company_name: Optional[str]
    customer_address_line1: Optional[str]
    customer_address_line2: Optional[str]
    city: Optional[str]
    state: Optional[str]
    pincode_no: Optional[str]
    gst: Optional[str]
    date_of_received: Optional[datetime]
    # created_by: Optional[int]
    # updated_by: Optional[int]
    test_type: Optional[str]
    product: Optional[int]
    batches: Optional[List[BatchUpdate]]
    test_params: Optional[List[RegistrationTestParamsUpdate]]

# class RegistrationWithBatchesUpdate(BaseModel):
#     registration: Optional[RegistrationUpdate]
#     batches: Optional[List[BatchUpdate]]

# class RegistrationWithBatchesGet(BaseModel):
#     registration: Optional[RegistrationSchema]
#     batches: Optional[List[BatchSchema]]

class RegistrationWithBatchesGet(BaseModel):
    registrations: Optional[RegistrationSchema]
    # batches: Optional[List[BatchSchema]]

class RegistrationsGet(BaseModel):
    registrations: Optional[RegistrationWithBatchesGet]

class SampleTestParamsCreate(BaseModel):
    test_parameter_id : int
    test_type  :  Optional[str]


class SampleCreate(BaseModel):
    sample_id: str
    name: str
    batch_id: int
    test_params : list[SampleTestParamsCreate]