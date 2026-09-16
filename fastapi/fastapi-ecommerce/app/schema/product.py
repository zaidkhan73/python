from pydantic import BaseModel, EmailStr, Field, AnyUrl, field_validator, model_validator, computed_field
from typing import Annotated, Literal, Optional, List
from uuid import UUID
from datetime import datetime


class Seller(BaseModel):
    id: UUID
    name: Annotated[
        str,
        Field(
            min_length=2,
            max_length=60,
            title="Seller Name",
            description="Name of the seller",
        ),
    ]
    email: EmailStr
    website: AnyUrl

    @field_validator("email", mode="after")
    @classmethod
    def validate_seller_email_domain(cls, value: EmailStr):
        allowed_domains = ["example.com", "ecommerce.com"]
        if "@" not in value:
            raise ValueError("Invalid email format")
        domain = str(value).split("@")[1]
        if domain not in allowed_domains:
            raise ValueError(
                f"Email domain must be one of the following: {', '.join(allowed_domains)}"
            )
        return value

    

class Product(BaseModel):
    id: UUID
    sku: Annotated[
        str,
        Field(
            min_length=1,
            max_length=20,
            title="SKU",
            description="Stock Keeping Unit (SKU)",
        ),
    ]
    name: Annotated[
        str,
        Field(
            min_length=3,
            max_length=50,
            title="Product Name",
            description="Name of the product",
        ),
    ]
    description: Annotated[
        str, Field(max_length=200, description="Description of the product")
    ]
    currency: Literal["INR"] = "INR"
    discount_percent: Annotated[
        float,
        Field(
            ge=0,
            le=100,
            title="Discount Percent",
            description="Discount percentage for the product",
        ),
    ]
    stock: Annotated[
        int, Field(ge=0, title="Stock", description="Available stock for the product")
    ]
    is_active: Annotated[
        bool,
        Field(
            title="Is Active", description="Indicates if the product is active or not"
        ),
    ]
    tags: Annotated[
        Optional[List[str]],
        Field(
            default=None,
            max_length=10,
            title="Tags",
            description="List of tags associated with the product (upto 10 tags)",
        ),
    ]
    image_urls: Annotated[
        List[AnyUrl],
        Field(
            min_length=1,
            max_length=5,
            title="Image URLs",
            description="List of image URLs for the product (upto 5 images)",
        ),
    ]
    created_at: datetime

    @field_validator("sku", mode="after") #used to work on one field after it has been validated
    @classmethod
    def validate_sku_format(cls, value: str):
        if "-" not in value:
            raise ValueError("SKU must contain a hyphen (-) to separate parts")

        last = value.split("-")[-1]
        if not (len(last) == 3 and last.isdigit()):
            raise ValueError(
                "SKU must end with a 3-digit number after the hyphen (e.g., 'ABC-123')"
            )

        return value

    @model_validator(mode="after") #used to work on the entire model after all fields have been validated
    @classmethod
    def validate_business_rules(cls, model: "Product"):
        if model.stock == 0 and model.is_active is True:
            raise ValueError("Product cannot be active if stock is zero")

        if model.discount_percent > 0 and model.rating == 0:
            raise ValueError(
                "Product cannot have a discount if the rating is zero"
            )

        return model

    @computed_field
    @property
    def final_price(self) -> float:
        return round(self.price * (1 - self.discount_percent / 100), 2)

