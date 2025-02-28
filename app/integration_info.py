integration_data = {  
    "data": {  
        "date": {  
            "created_at": "2025-02-20",  
            "updated_at": "2025-02-22"  
        },  
        "descriptions": {  
            "app_description": "Fetches the number of likes and reposts for a specified LinkedIn post at regular intervals.",  
            "app_logo": "https://iili.io/Jcshqe2.md.webp",  
            "app_name": "Post-Stats-Tracker",  
            "app_url": "https://hngx-stage3-telex-integration-linkedin.vercel.app",  
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
                "default": "https://www.linkedin.com/feed/update/urn:li:activity:7300033040125169665"  
            },  
            {  
                "label": "Update Interval",  
                "type": "text",  
                "required": True,  
                "default": "*/1 * * * *"  #10mn for testing then 6hours "0 */6 * * *"  
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
        ],  
        "tick_url": "https://hngx-stage3-telex-integration-linkedin.vercel.app/tick",  
        "target_url": ""  
    }  
}