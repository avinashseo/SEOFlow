"""
SEOFlow Product Model

Every module in SEOFlow works with Product objects.
No module should directly access CSV columns.

"""

from dataclasses import dataclass

@dataclass(slots=True)
class Product:

    # Basic Information
    name: str
    slug: str
    url: str

    # Hero Section 
    hero_title: str
    hero_text: str

    # SEO 
    meta_title: str
    meta_description: str
    og_title: str = ""
    og_description: str = ""


    # Imge Optimization 
    image_url: str = ""
    image_alt: str = ""

    # Content
    applications: str =  ""  
    benefits: str = ""

    # Product Information
    pack_sizes: str = ""
    moq: str = ""
    lead_time: str = ""
    shelf_life: str = ""
    

    @classmethod
    def from_dict(cls, data:dict):
        return cls(**data)