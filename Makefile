PROJECT_NAME=cncdnua
PYTHONPATH=$(CURDIR):$(CURDIR)/$(PROJECT_NAME)
MANAGE=PYTHONPATH=$(PYTHONPATH) python $(PROJECT_NAME)/manage.py
LOCAL_SETTINGS=--settings=cncdnua.settings.local

run:
	$(MANAGE) runserver $(LOCAL_SETTINGS)

syncdb:
	$(MANAGE) syncdb $(LOCAL_SETTINGS)
	$(MANAGE) migrate $(LOCAL_SETTINGS)
