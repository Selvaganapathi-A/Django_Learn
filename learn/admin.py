from django.contrib import admin

from .model import Event, Participant, Venue


# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (
        ("name", "venue"),
        "event_date",
        "description",
        "event_manager",
    )
    list_display = (
        "name",
        "event_date",
        "venue",
    )
    list_filter = (
        "event_date",
        "venue",
    )
    ordering = ("-event_date",)
    search_fields = (
        "name",
        "description",
    )


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "address",
        "phone",
    )
    list_filter = (
        "name",
        "address",
        "website",
    )
    ordering = ("name",)
    search_fields = (
        "name",
        "address",
    )


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = (
        "firstname",
        "lastname",
        "email",
    )
    ordering = (
        "lastname",
        "firstname",
    )
    search_fields = (
        "firstname",
        "lastname",
    )


# _changeform_view, _create_formsets, _delete_view,
# _filter_actions_by_permissions, _get_action_description, _get_base_actions,
# _get_edited_object_pks, _get_form_for_get_fields, _get_list_editable_queryset,
# _get_obj_does_not_exist_redirect, _response_post_save, action_checkbox,
# action_form, actions, actions_on_bottom, actions_on_top,
# actions_selection_counter, add_form_template, add_view, autocomplete_fields,
# change_form_template, change_list_template, change_view, changeform_view,
# changelist_view, check, checks_class, construct_change_message,
# date_hierarchy, delete_confirmation_template, delete_model, delete_queryset,
# delete_selected_confirmation_template, delete_view, exclude, fields,
# fieldsets, filter_horizontal, filter_vertical, form,
# formfield_for_choice_field, formfield_for_dbfield, formfield_for_foreignkey,
# formfield_for_manytomany, formfield_overrides, get_action, get_action_choices,
# get_actions, get_autocomplete_fields, get_changeform_initial_data,
# get_changelist, get_changelist_form, get_changelist_formset,
# get_changelist_instance, get_deleted_objects, get_empty_value_display,
# get_exclude, get_field_queryset, get_fields, get_fieldsets, get_form,
# get_formset_kwargs, get_formsets_with_inlines, get_inline_formsets,
# get_inline_instances, get_inlines, get_list_display, get_list_display_links,
# get_list_filter, get_list_select_related, get_model_perms, get_object,
# get_ordering, get_paginator, get_prepopulated_fields, get_preserved_filters,
# get_queryset, get_readonly_fields, get_search_fields, get_search_results,
# get_sortable_by, get_urls, get_view_on_site_url, has_add_permission,
# has_change_permission, has_delete_permission, has_module_permission,
# has_view_or_change_permission, has_view_permission, history_view, inlines,
# list_display, list_display_links, list_editable, list_filter,
# list_max_show_all, list_per_page, list_select_related, log_addition,
# log_change, log_deletion, lookup_allowed, media, message_user,
# object_history_template, ordering, paginator, popup_response_template,
# prepopulated_fields, preserve_filters, radio_fields, raw_id_fields,
# readonly_fields, render_change_form, render_delete_form, response_action,
# response_add, response_change, response_delete, response_post_save_add,
# response_post_save_change, save_as, save_as_continue, save_form,
# save_formset, save_model, save_on_top, save_related, search_fields,
# search_help_text, show_full_result_count, sortable_by, to_field_allowed,
# urls, view_on_site
