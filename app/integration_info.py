integration_data = {  
    "data": {  
        "date": {  
            "created_at": "2025-02-20",  
            "updated_at": "2025-02-20"  
        },  
        "descriptions": {  
            "app_description": "Fetches the number of likes and reposts for a specified LinkedIn post at regular intervals.",  
            "app_logo": "https://iili.io/Jcshqe2.md.webp",  
            "app_name": "Post-Stats-Tracker",  
            "app_url": "http://54.242.222.191",  
            "background_color": "#0077B5"  
        },  
        "integration_category": "Monitoring & Logging",  
        "integration_type": "interval",  
        "is_active": True,  
        "output": [  
            {  
                "label": "Telex Channel for Likes",  
                "value": True  
            },  
            {  
                "label": "Telex Channel for Reposts",  
                "value": True  
            }  
        ],  
        "key_features": [  
            "Fetches likes and repost counts for LinkedIn posts.",  
            "Updates every six hours.",  
            "Sends notifications to designated Telex channels.",  
            "Customizable settings for post URL."  
        ],  
        "permissions": {  
            "monitoring_user": {  
                "always_online": True,  
                "display_name": "Post Stats Monitor"  
            }  
        },  
        "settings": [  
            {  
                "label": "Post URL",  
                "type": "text",  
                "required": True,  
                "default": "https://www.linkedin.com/company/center-for-epidemiological-modelling-and-analysis-cema-africa/posts?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3BCPf5AmcIScGS6G%2BYTXsUbw%3D%3D"  
            },  
            {  
                "label": "Update Interval",  
                "type": "text",  
                "required": True,  
                "default": "0 */6 * * *"  
            },  
            {  
                "label": "LinkedIn API Key",  
                "type": "text",  
                "required": True,  
                "default": "YOUR_API_KEY"  
            },  
            {  
                "label": "Alert Admin on Errors",  
                "type": "checkbox",  
                "required": True,  
                "default": "Yes"  
            },  
            {  
                "label": "Sensitivity Level",  
                "type": "dropdown",  
                "required": True,  
                "default": "Low",  
                "options": ["High", "Medium", "Low"]  
            },  
            {  
                "label": "Notify Users",  
                "type": "multi-checkbox",  
                "required": True,  
                "default": "User-1",  
                "options": ["User-1", "User-2", "User-3", "User-4"]  
            }  
        ],  
        "tick_url": "http://54.242.222.191/tick",  
        "target_url": ""  
    }  
}