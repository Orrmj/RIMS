from PyQt5.QtCore import QObject, pyqtSignal


class Model(QObject):
  
    # INSPECTION DETAILS
    #Group TextBoxes
    #input_inspection_details_assessment_team_changed = None
    
    #Group DatePicker
    #input_inspection_details_date_assessment_changed = None
    
    #Group LineEdits
    #input_inspection_details_crossing_location_changed = None 
    #input_inspection_details_latitude_changed = None 
    #input_inspection_details_location_number_changed = None 
    #input_inspection_details_longitude_changed = None 
    #input_inspection_details_municipality_changed = None 
    #input_inspection_details_road_name_changed = None 
    #input_inspection_details_road_number_changed = None 
    #input_inspection_details_spur_mile_changed = None 
    #input_inspection_details_spur_name_changed = None 
    #input_inspection_details_subdivision_mile_changed = None 

    #Group ComboBoxes
    input_inspection_details_gcws_type_changed = pyqtSignal(list)
    input_inspection_details_grade_crossing_type_changed = pyqtSignal(list)
    #input_inspection_details_province_changed = None
    #input_inspection_details_railway_authority_changed = None
    #input_inspection_details_reason_for_assessment_changed = None
    #input_inspection_details_road_authority_changed = None
    #input_inspection_details_subdivision_name_changed = None
    #input_inspection_details_track_type_changed = None

    # COLLISION HISTORY (5 YEAR PERIOD)
    #Group TextEdits
    #input_collision_history_comments_changed = None

    #Group LineEdits
    input_collision_history_fatal_injury_changed = pyqtSignal(int) 
    #input_collision_history_fatalities_changed = None 
    #input_collision_history_personal_injuries_changed = None 
    input_collision_history_personal_injury_changed = pyqtSignal(int) 
    input_collision_history_property_damage_changed = pyqtSignal(int)

    #Group Labels
    input_collision_history_total_5_year_period_changed = pyqtSignal(int)

    # GENERAL INFORMATION
    #Group TextEdits
    #input_general_info_comments_changed = None

    #Group LineEdits
    #input_general_info_observe_special_buildings_changed = None 
    input_general_info_rail_max_railway_operating_speed_freight_changed = pyqtSignal(int) 
    input_general_info_rail_max_railway_operating_speed_passenger_changed = pyqtSignal(int)  
    input_general_info_rail_no_trains_per_day_freight_changed = pyqtSignal(int)  
    input_general_info_rail_no_trains_per_day_passengers_changed = pyqtSignal(int)
    input_general_info_rail_no_tracks_main_changed = pyqtSignal(int)
    input_general_info_rail_no_tracks_other_changed = pyqtSignal(int)
    input_general_info_rail_railway_design_speed_changed = pyqtSignal(int)  
    input_general_info_road_aadt_current_changed = pyqtSignal(int)  
    input_general_info_road_aadt_forecast_changed = pyqtSignal(int)  
    #input_general_info_road_aadt_year_current_changed = None 
    #input_general_info_road_aadt_year_forecasted_changed = None 
    #input_general_info_road_cyclist_per_day_changed = None 
    input_general_info_road_no_traffic_lanes_bidirectional_changed = pyqtSignal(int)  
    input_general_info_road_no_traffic_lanes_northbound_or_eastbound_changed = pyqtSignal(int)  
    input_general_info_road_no_traffic_lanes_southbound_or_westbound_changed = pyqtSignal(int)  
    #input_general_info_road_other_users_changed = None 
    #input_general_info_road_other_users_daily_users_changed = None 
    #input_general_info_road_pedestrians_per_day_changed = None 
    input_general_info_road_speed_design_changed = pyqtSignal(int)  
    #input_general_info_road_speed_posted_changed = None 

    #Group ComboBoxes
    #input_general_info_observe_roadway_illumination_changed = None
    #input_general_info_observe_surrounding_land_use_changed = None
    #input_general_info_rail_train_switching_changed = None        
    #input_general_info_road_assistive_pedestrian_devices_changed = None
    input_general_info_road_classification_changed = pyqtSignal(list)        
    #input_general_info_road_dangerous_goods_route_changed = None
    #input_general_info_road_school_bus_route_changed = None
    #input_general_info_road_seasonal_volume_fluctuations_changed = None
    input_general_info_road_sidewalks_changed = pyqtSignal(list)

    #Group Labels
    input_general_info_rail_no_tracks_total_changed = pyqtSignal(int)
    input_general_info_rail_no_trains_per_day_total_changed = pyqtSignal(int)
    input_general_info_road_no_traffic_lanes_total_changed = pyqtSignal(int)

    # DESIGN CONSIDERATIONS (GCS SECTION 10)
    #Group TextEdits
    #input_design_comments_changed = None

    #Group LineEdits
    input_design_measure_adjacent_track_clearance_distance_changed = pyqtSignal(float)
    input_design_measure_adjacent_track_separation_distance_changed = pyqtSignal(float) 
    input_design_measure_clearance_distance_pedestrian_changed = pyqtSignal(float)
    input_design_measure_clearance_distance_vehicle_changed = pyqtSignal(float) 
    input_design_road_max_approach_grade_within_s_changed = pyqtSignal(float) 

    #Group ComboBoxes
    #input_design_observe_field_acceleration_times_exceed_td = None
    input_design_road_design_vehicle_type_changed = pyqtSignal(list)

    #Group Labels
    input_design_calculate_adjacent_track_clearance_time_changed = pyqtSignal(float)
    input_design_calculate_clearance_time_crossing_pedestrian_design_check_changed = pyqtSignal(float)
    input_design_calculate_clearance_time_crossing_vehicle_design_check_changed = pyqtSignal(float)
    input_design_calculate_clearance_time_gate_arm_ssd_changed = pyqtSignal(float)
    input_design_calculate_clearance_time_gate_arm_stop_changed = pyqtSignal(float)
    input_design_calculate_vehicle_travel_distance_changed = pyqtSignal(float)
    input_design_input_reaction_time_changed = pyqtSignal(float)
    input_design_lookup_design_vehicle_class_changed = pyqtSignal(str)
    input_design_lookup_design_vehicle_length_changed = pyqtSignal(float)
    input_design_lookup_grade_adjustment_factor_changed = pyqtSignal(float)
    input_design_lookup_vehicle_departure_time_crossing_changed = pyqtSignal(float)
    input_design_lookup_vehicle_departure_time_gate_arm_clearance_changed = pyqtSignal(float)
    
    # LOCATION OF GRADE CROSSING (GCS SECTION 11)
    #Group TextEdits
    #input_location_of_grade_crossing_comments_changed = None

    #Group LineEdits
    #input_location_of_grade_crossing_nearest_intersection_other_n_or_e_approach_changed = None 
    #input_location_of_grade_crossing_nearest_intersection_other_s_of_w_approach_changed = None 
    input_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach_changed = pyqtSignal(float) 
    input_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach_changed = pyqtSignal(float)  
    input_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach_changed = pyqtSignal(float)  
    input_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach_changed = pyqtSignal(float)  

    #group ComboBoxes
    #input_location_of_grade_crossing_observe_nearby_pedestrian_crosswalk_changed = None
    #input_location_of_grade_crossing_queue_condition_changed = None
    #input_location_of_grade_crossing_visibility_of_warning_lights_changed = None
    
    # GRADE CROSSING SURFACE (GCS SECTION 5)
    #Group TextEdits
    #input_grade_crossing_surface_comments_changed = None

    #Group LineEdits
    #input_grade_crossing_surface_measure_crossing_surface_extension_n_or_e_approach_changed = None 
    #input_grade_crossing_surface_measure_crossing_surface_extension_s_or_w_approach_changed = None 
    #input_grade_crossing_surface_measure_crossing_surface_width_changed = None 
    #input_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_n_or_e_approach_changed = None 
    #input_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_s_or_w_approach_changed = None 
    #input_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_n_or_e_approach_changed = None 
    #input_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_s_or_w_approach_changed = None 
    #input_grade_crossing_surface_measure_elevation_top_of_rail_above_road_surface_changed = None 
    #input_grade_crossing_surface_measure_elevation_top_of_rail_below_road_surface_changed = None 
    #input_grade_crossing_surface_measure_flangeway_depth_changed = None 
    #input_grade_crossing_surface_measure_flangeway_width_changed = None 
    #input_grade_crossing_surface_measure_road_surface_median_width_changed = None 
    #input_grade_crossing_surface_measure_road_surface_shoulder_n_or_e_approach_changed = None 
    #input_grade_crossing_surface_measure_road_surface_shoulder_s_or_w_approach_changed = None 
    #input_grade_crossing_surface_measure_road_surface_travel_lanes_width_n_or_e_approach_changed = None 
    #input_grade_crossing_surface_measure_road_surface_travel_lanes_width_s_or_w_approach_changed = None 
    #input_grade_crossing_surface_measure_side_grinding_depth_changed = None 
    #input_grade_crossing_surface_measure_side_grinding_width_changed = None 
    #input_grade_crossing_surface_measure_sidewalk_extension_n_or_e_approach_changed = None 
    #input_grade_crossing_surface_measure_sidewalk_extension_s_or_w_approach_changed = None 
    #input_grade_crossing_surface_measure_sidewalk_width_n_or_e_approach_changed = None 
    #input_grade_crossing_surface_measure_sidewalk_width_s_or_w_approach_changed = None 

    #Group ComboBoxes
    #input_grade_crossing_surface_observe_crossing_smoothness_changed = None
    #input_grade_crossing_surface_observe_crossing_surface_condition_changed = None
    #input_grade_crossing_surface_observe_material_changed = None
    #input_grade_crossing_surface_observe_road_approach_surface_condition_changed = None
    #input_grade_crossing_surface_observe_road_approach_surface_type_changed = None

    # ROAD GEOMETRY (GCS SECTION 6)
    #Group TextEdits 
    #input_road_geometry_comments_changed = None

    #Group LineEdits
    input_road_geometry_measure_railway_cross_slope_changed = pyqtSignal(float) 
    #input_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_n_or_e_approach_changed = None 
    #input_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_s_or_w_approach_changed = None 
    #input_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_n_or_e_approach_changed = None 
    #input_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_s_or_w_approach_changed = None 
    input_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach_changed = pyqtSignal(float)
    input_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach_changed = pyqtSignal(float)
    input_road_geometry_rail_superelevation_n_or_e_approach_changed = pyqtSignal(float) 
    input_road_geometry_rail_superelevation_s_or_w_approach_changed = pyqtSignal(float) 
    #input_road_geometry_road_crossing_angle_changed = None 
    input_road_geometry_road_general_approach_grade_n_or_e_approach_changed = pyqtSignal(float)  
    input_road_geometry_road_general_approach_grade_s_or_w_approach_changed = pyqtSignal(float) 

    #Group ComboBoxes
    #input_road_geometry_observe_lane_width_crossing_vs_approach_n_or_e_approach_changed = None
    #input_road_geometry_observe_lane_width_crossing_vs_approach_s_or_w_approach_changed = None
    #input_road_geometry_observe_low_bed_truck_condition_changed = None
    #input_road_geometry_observe_smooth_alignment_within_ssd_n_or_e_approach_changed = None
    #input_road_geometry_observe_smooth_alignment_within_ssd_s_or_w_approach_changed = None
    
    #Group Labels
    input_road_geometry_lookup_gradient_difference_changed = pyqtSignal(float)
    
    # SIGHTLINES (GCS SECTION 7)
    #Group TextEdits
    #input_sightlines_comments_changed = None
    
    #Group LineEdits
    #input_sightlines_measure_dssd_actual_n_or_e_approach_left_changed = None 
    #input_sightlines_measure_dssd_actual_n_or_e_approach_right_changed = None 
    #input_sightlines_measure_dssd_actual_s_or_w_approach_left_changed = None 
    #input_sightlines_measure_dssd_actual_s_or_w_approach_right_changed = None 
    #input_sightlines_measure_dstopped_actual_n_or_e_approach_driver_left_changed = None 
    #input_sightlines_measure_dstopped_actual_n_or_e_approach_driver_right_changed = None 
    #input_sightlines_measure_dstopped_actual_s_or_w_approach_driver_left_changed = None 
    #input_sightlines_measure_dstopped_actual_s_or_w_approach_driver_right_changed = None 
    #input_sightlines_measure_ssd_actual_n_or_e_approach_changed = None 
    #input_sightlines_measure_ssd_actual_s_or_w_approach_changed = None 

    #Group ComboBoxes
    #input_sightlines_observe_sightline_obstructions_changed = None

    #Group Labels
    input_sightlines_calculate_dssd_vehicle_min_ft_changed = pyqtSignal(float)
    input_sightlines_calculate_dssd_vehicle_min_m_changed = pyqtSignal(float)
    input_sightlines_calculate_dstopped_pedestrian_min_ft_changed = pyqtSignal(float)
    input_sightlines_calculate_dstopped_pedestrian_min_m_changed = pyqtSignal(float)
    input_sightlines_calculate_dstopped_vehicle_min_ft_changed = pyqtSignal(float)
    input_sightlines_calculate_dstopped_vehicle_min_m_changed = pyqtSignal(float)
    input_sightlines_lookup_ssd_minimum_n_or_e_approach_changed = pyqtSignal(float)
    input_sightlines_lookup_ssd_minimum_s_or_w_approach_changed = pyqtSignal(float)

    # SIGNS AND PAVEMENT MARKINGS (GCS SECTION 8)
    #Group TextEdits
    #DELETE input_signs_and_markings_advisory_speed_comments_changed = None
    #DELETE input_signs_and_markings_comments_changed = None
    #DELETE input_signs_and_markings_emergency_notification_comments_changed = None
    #DELETE input_signs_and_markings_number_of_tracks_comments_changed = None
    #DELETE input_signs_and_markings_railway_crossing_ahead_comments_changed = None
    #DELETE input_signs_and_markings_railway_crossing_comments_changed = None
    #DELETE input_signs_and_markings_stop_comments_changed = None
    #DELETE input_signs_and_markings_stop_sign_ahead_comments_changed = None

    #Group LineEdits
    #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_rail_changed = None 
    #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_road_changed = None 
    #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_height_changed = None 
    #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_rail_changed = None 
    #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_road_changed = None 
    #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_height_changed = None 
    #input_signs_and_markings_stop_n_or_e_approach_height_changed = None 
    #input_signs_and_markings_stop_n_or_e_approach_location_from_rail_changed = None 
    #input_signs_and_markings_stop_n_or_e_approach_location_from_road_changed = None 
    #input_signs_and_markings_stop_s_or_w_approach_height_changed = None 
    #input_signs_and_markings_stop_s_or_w_approach_location_from_rail_changed = None 
    #input_signs_and_markings_stop_s_or_w_approach_location_from_road_changed = None 
    #input_signs_and_markings_stop_sign_ahead_n_or_e_approach_height_changed = None 
    #input_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_rail_changed = None 
    #input_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_road_changed = None 
    #input_signs_and_markings_stop_sign_ahead_s_or_w_approach_height_changed = None 
    #input_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_rail_changed = None 
    #input_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_road_changed = None 

    #Group ComboBoxes
    #input_signs_and_markings_advisory_speed_n_or_e_approach_present_changed = None
    #input_signs_and_markings_advisory_speed_n_or_e_approach_with_wa_18_20_changed = None
    #input_signs_and_markings_advisory_speed_s_or_w_approach_present_changed = None
    #input_signs_and_markings_advisory_speed_s_or_w_approach_with_wa_18_20_changed = None
    #input_signs_and_markings_dividing_lines_present_changed = None
    #input_signs_and_markings_emergency_notification_n_or_e_approach_condition_changed = None
    #input_signs_and_markings_emergency_notification_n_or_e_approach_legible_changed = None
    #input_signs_and_markings_emergency_Notification_n_or_e_approach_orientation_changed = None
    #input_signs_and_markings_emergency_notification_n_or_e_approach_present_changed = None
    #input_signs_and_markings_emergency_notification_s_or_w_approach_condition_changed = None
    #input_signs_and_markings_emergency_notification_s_or_w_approach_legible_changed = None
    #input_signs_and_markings_emergency_notification_s_or_w_approach_orientation_changed = None
    #input_signs_and_markings_emergency_notification_s_or_w_approach_present_changed = None
    #input_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_1b_changed = None
    #input_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_3c_changed = None
    #input_signs_and_markings_number_of_tracks_n_or_e_approach_present_changed = None
    #input_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_1b_changed = None
    #input_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_3c_changed = None
    #input_signs_and_markings_number_of_tracks_s_or_w_approach_present_changed = None
    #input_signs_and_markings_per_mutcd_changed = None
    #input_signs_and_markings_posted_speed_n_or_e_approach_present_changed = None
    #input_signs_and_markings_posted_speed_s_or_w_approach_present_changed = None
    #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_orientation_changed = None
    #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_present_changed = None
    #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_orientation_changed = None
    #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_present_changed = None
    #input_signs_and_markings_railway_crossing_n_or_e_approach_per_fig_8_1a_changed = None
    #input_signs_and_markings_railway_crossing_n_or_e_approach_present_changed = None
    #input_signs_and_markings_railway_crossing_s_or_w_approach_per_fig_8_1a_changed = None
    #input_signs_and_markings_railway_crossing_s_or_w_approach_present_changed = None
    #input_signs_and_markings_sidewalks_present_changed = None
    #input_signs_and_markings_stop_n_or_e_approach_per_fig_8_4_changed = None
    #input_signs_and_markings_stop_n_or_e_approach_present_changed = None
    #input_signs_and_markings_stop_n_or_e_approach_same_post_changed = None
    #input_signs_and_markings_stop_s_or_w_approach_per_fig_8_4_changed = None
    #input_signs_and_markings_stop_s_or_w_approach_present_changed = None
    #input_signs_and_markings_stop_s_or_w_approach_same_post_changed = None
    #input_signs_and_markings_stop_sign_ahead_n_or_e_approach_present_changed = None
    #input_signs_and_markings_stop_sign_ahead_s_or_w_approach_present_changed = None

    # GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)
    # Group Labels
    input_gcws_warrant_private_9_3_changed = pyqtSignal(str)
    input_gcws_warrant_private_9_3_1_changed = pyqtSignal(str)
    input_gcws_warrant_private_9_3_2_a_changed = pyqtSignal(str)
    input_gcws_warrant_private_9_3_2_b_changed = pyqtSignal(str)
    input_gcws_warrant_private_9_3_2_c_changed = pyqtSignal(str)
    input_gcws_warrant_public_9_1_changed = pyqtSignal(str)
    input_gcws_warrant_public_9_1_a_changed = pyqtSignal(str)
    input_gcws_warrant_public_9_1_b_changed = pyqtSignal(str)
    input_gcws_warrant_public_9_1_c_changed = pyqtSignal(str)
    input_gcws_warrant_public_9_1_d_i_changed = pyqtSignal(str)
    input_gcws_warrant_public_9_1_d_ii_changed = pyqtSignal(str)
    input_gcws_warrant_public_9_1_d_iii_changed = pyqtSignal(str)
    input_gcws_warrant_sidewalk_9_5_changed = pyqtSignal(str)
    input_gates_gcws_warrant_private_9_4_1_a_changed = pyqtSignal(str)
    input_gates_gcws_warrant_private_9_4_1_b_changed = pyqtSignal(str)
    input_gates_gcws_warrant_private_9_4_1_c_changed = pyqtSignal(str)
    input_gates_gcws_warrant_public_9_2_1_a_changed = pyqtSignal(str)
    input_gates_gcws_warrant_public_9_2_1_b_changed = pyqtSignal(str)
    input_gates_gcws_warrant_public_9_2_1_c_changed = pyqtSignal(str)
    input_gates_gcws_warrant_public_9_2_1_d_changed = pyqtSignal(str)
    input_gates_gcws_warrant_public_9_2_1_e_changed = pyqtSignal(str)
    input_gates_gcws_warrant_sidewalk_9_6_changed = pyqtSignal(str)
    #input_gcws_warrants_comments_changed = None

    # GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)
    #Group TextEdits
    #input_gcws_comments_changed = None
        
    #Group LineEdits
    #input_gcws_measure_warning_device_n_or_e_approach_distance_from_rail_changed = None 
    #input_gcws_measure_warning_device_n_or_e_approach_distance_from_road_changed = None 
    #input_gcws_measure_warning_device_n_or_e_approach_distance_top_of_foundation_changed = None 
    #input_gcws_measure_warning_device_n_or_e_approach_slope_from_foundation_changed = None 
    #input_gcws_measure_warning_device_s_or_w_approach_distance_from_rail_changed = None 
    #input_gcws_measure_warning_device_s_or_w_approach_distance_from_road_changed = None 
    #input_gcws_measure_warning_device_s_or_w_approach_distance_top_of_foundation_changed = None 
    #input_gcws_measure_warning_device_s_or_w_approach_slope_from_foundation_changed = None 
    #input_gcws_rail_crossing_warning_time_actual_changed = None 

    #Group ComboBox
    #input_gcws_observe_bell_if_sidewalk_changed = None
    #input_gcws_observe_bells_condition_changed = None
    #input_gcws_observe_bells_n_or_e_approach_changed = None
    #input_gcws_observe_bells_s_or_w_approach_changed = None
    #input_gcws_observe_cantilever_lights_condition_changed = None
    #input_gcws_observe_cantilever_lights_n_or_e_approach_changed = None
    #input_gcws_observe_cantilever_lights_s_or_w_approach_changed = None
    #input_gcws_observe_gates_condition_changed = None
    #input_gcws_observe_gates_n_or_e_approach_changed = None
    #input_gcws_observe_gates_s_or_w_approach_changed = None
    #input_gcws_observe_gcws_limited_use_with_walk_light_assembly_changed = None
    #input_gcws_observe_gcws_limited_use_without_walk_light_assembly_changed = None
    #input_gcws_observe_light_units_condition_changed = None
    #input_gcws_observe_light_units_n_or_e_approach_changed = None
    #input_gcws_observe_light_units_s_or_w_approach_changed = None
    #input_gcws_observe_warning_time_consistency_changed = None   
    #input_gcws_observe_warning_time_consistency_reduced_speed_changed = None
    #input_gcws_rail_cut_out_circuit_requirements_changed = None
    #input_gcws_rail_directional_stick_circuit_requirements_changed = None
    #input_gcws_rail_self_diagnostic_changed = None

    #Group Labels
    input_gcws_rail_design_approach_warning_time_changed = pyqtSignal(float)
    input_gcws_rail_design_warning_time_adjacent_crossing_changed = pyqtSignal(float)
    input_gcws_rail_design_warning_time_clearance_distance_changed = pyqtSignal(float)
    input_gcws_rail_design_warning_time_departure_time_pedestrian_changed = pyqtSignal(float)
    input_gcws_rail_design_warning_time_departure_time_vehicle_changed = pyqtSignal(float)
    input_gcws_rail_design_warning_time_gate_arm_clearance_changed = pyqtSignal(float)
    input_gcws_rail_design_warning_time_preemption_changed = pyqtSignal(float)
    input_gcws_rail_design_warning_time_ssd_changed = pyqtSignal(float)

    # FLASHING LIGHT UNITS (GCS SECTION 13 & 14)
    #Group TextEdits
    #input_light_units_comments_changed = None

    #Group LineEdits
    #input_light_units_measure_cantilevers_n_or_e_approach_distance_from_rail_changed = None 
    #input_light_units_measure_cantilevers_n_or_e_approach_distance_from_road_changed = None 
    #input_light_units_measure_cantilevers_n_or_e_approach_dl_changed = None 
    #input_light_units_measure_cantilevers_n_or_e_approach_dr_changed = None 
    #input_light_units_measure_cantilevers_n_or_e_approach_height_changed = None 
    #input_light_units_measure_cantilevers_s_or_w_approach_distance_from_rail_changed = None 
    #input_light_units_measure_cantilevers_s_or_w_approach_distance_from_road_changed = None 
    #input_light_units_measure_cantilevers_s_or_w_approach_dl_changed = None 
    #input_light_units_measure_cantilevers_s_or_w_approach_dr_changed = None 
    #input_light_units_measure_cantilevers_s_or_w_approach_height_changed = None 
    #input_light_units_measure_n_or_e_approach_height_changed = None 
    #input_light_units_measure_s_or_w_approach_height_changed = None 

    #Group ComboBoxes
    #input_light_units_observe_cantilevers_per_fig_12_3_changed = None
    #input_light_units_observe_per_fig_12_1_changed = None
    #input_light_units_observe_sidewalks_n_or_e_approach_changed = None
    #input_light_units_observe_sidewalks_s_or_w_approach_changed = None
    #input_light_units_observe_supplemental_lights_n_or_e_approach_changed = None
    #input_light_units_observe_supplemental_lights_s_or_w_approach_changed = None
    #input_light_units_observe_visibility_back_lights_n_or_e_approach_changed = None
    #input_light_units_observe_visibility_back_lights_s_or_w_approach_changed = None
    #input_light_units_observe_visibility_front_lights_n_or_e_approach_changed = None
    #input_light_units_observe_visibility_front_lights_s_or_w_approach_changed = None

    # GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)
    #Group TextEdits
    #input_gates_gcws_comments_changed = None

    #Group LineEdits
    #input_gates_gcws_measure_distance_between_gate_end_and_road_cl_n_or_e_approach_changed = None 
    #input_gates_gcws_measure_distance_between_gate_end_and_road_cl_s_or_w_approach_changed = None 
    #input_gates_gcws_measure_gate_ascent_time_changed = None 
    #input_gates_gcws_measure_gate_descent_time_changed = None 
    #input_gates_gcws_rail_gate_arm_delay_time_design_changed = None 
    input_gates_gcws_rail_gate_arm_descent_time_design_changed = pyqtSignal(float) 
    #input_gates_gcws_rail_inner_gate_arm_delay_time_design_changed = None 

    #Group Labels
    input_gates_gcws_calculate_gate_arm_clearance_time_recommended_changed = pyqtSignal(float)
    input_gates_gcws_calculate_inner_gate_arm_delay_time_recommended_changed = pyqtSignal(float)

    #Group ComboBoxes
    #input_gates_gcws_observe_gate_arm_rest_changed = None
    #input_gates_gcws_observe_gate_ascent_time_changed = None
    #input_gates_gcws_observe_gate_descent_time_changed = None
    #input_gates_gcws_observe_gate_strips_n_or_e_approach_changed = None
    #input_gates_gcws_observe_gate_strips_s_or_w_approach_changed = None
    #input_gates_gcws_observe_per_fig_12_2_changed = None

    # PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)
    #Group Text Edits
    #input_aawd_comments_changed = None

    #Group LineEdits
    #input_aawd_measure_distance_sign_and_stop_n_or_e_approach_actual_changed = None 
    #input_aawd_measure_distance_sign_and_stop_s_or_w_approach_actual_changed = None 

    #Group ComboBoxes
    #input_aawd_observe_present_n_or_e_approach_changed = None
    #input_aawd_observe_present_s_or_w_approach_changed = None
    #input_aawd_road_aawd_sufficient_activation_time_n_or_e_approach_changed = None
    #input_aawd_road_aawd_sufficient_activation_time_s_or_w_approach_changed = None

    #Group Labels
    input_aawd_calculate_advance_activation_time_design_n_or_e_approach_changed = pyqtSignal(float)
    input_aawd_calculate_advance_activation_time_design_s_or_w_approach_changed = pyqtSignal(float)
    input_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended_changed = pyqtSignal(float)
    input_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended_changed = pyqtSignal(float)
    input_aawd_warrant_gcr_lookup_road_classification_changed = pyqtSignal(str)
    input_aawd_warrant_gcr_observe_environmental_condition_changed = pyqtSignal(str)
    input_aawd_warrant_gcr_observe_sightline_obstruction_changed = pyqtSignal(str)
    input_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr_changed = pyqtSignal(str)
    input_aawd_warrant_mutcd_lookup_significant_road_downgrade_changed = pyqtSignal(str)

    # INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)
    #Group TextEdits
    #input_preemption_of_traffic_signals_comments_changed = None

    #Group LineEdits
    #input_preemption_of_traffic_signals_road_preemption_warning_time_actual_changed = None 
    #input_preemption_of_traffic_signals_road_preemption_warning_time_design_changed = None 

    #Group CombBoxes
    #input_preemption_of_traffic_signals_observe_consideration_of_Longer_vehicles_changed = None
    #input_preemption_of_traffic_signals_observe_known_queuing_issues_changed = None
    #input_preemption_of_traffic_signals_observe_pedestrian_accommodation_changed = None
    #input_preemption_of_traffic_signals_observe_queuing_condition_changed = None
    #input_preemption_of_traffic_signals_observe_supplemental_signage_changed = None
    #input_preemption_of_traffic_signals_observe_traffic_clearance_time_adequate_changed = None
    #input_preemption_of_traffic_signals_observe_unintended_queuing_by_traffic_signals_changed = None
    #input_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type_changed = None

    #Group DatePicker
    #input_preemption_of_traffic_signals_road_date_Last_preemption_check_changed = None

    #Group Labels
    input_preemption_of_traffic_signals_lookup_proximity_condition_changed = pyqtSignal(str)
    input_preemption_of_traffic_signals_lookup_required_changed = pyqtSignal(str)

    # WHISTLE CESSATION (GCS SECTION Appendix D)
    #Group TextEdits
    #input_areas_without_train_whistling_comments_changed = None

    #Group ComboBoxes
    #input_areas_without_train_whistling_observe_for_stop_and_proceed_changed = None
    #input_areas_without_train_whistling_observe_tresNoneing_area_changed = None
    #input_areas_without_train_whistling_rail_anti_whistling_zone_changed = None
    #input_areas_without_train_whistling_rail_anti_whistling_zone_24_hrs_changed = None

    #Group Labels
    input_areas_without_train_whistling_lookup_gcs_12_to_16_changed = pyqtSignal(str)
    input_areas_without_train_whistling_lookup_gcs_9_2_changed = pyqtSignal(str)
    input_areas_without_train_whistling_requirements_observe_table_D1_changed = pyqtSignal(str)

    # INSPECTION DETAILS
    #Group TextBoxes
    #input_inspection_details_assessment_team = None
    
    #Group DatePicker
    #input_inspection_details_date_assessment = None
    
    #Group LineEdits
    #input_inspection_details_crossing_location = None 
    #input_inspection_details_latitude = None 
    #input_inspection_details_location_number = None 
    #input_inspection_details_longitude = None 
    #input_inspection_details_municipality = None 
    #input_inspection_details_road_name = None 
    #input_inspection_details_road_number = None 
    #input_inspection_details_spur_mile = None 
    #input_inspection_details_spur_name = None 
    #input_inspection_details_subdivision_mile = None 

    #Group ComboBoxes
    #input_inspection_details_gcws_type
    @property
    def input_inspection_details_gcws_type(self):
        return self._input_inspection_details_gcws_type

    @input_inspection_details_gcws_type.setter
    def input_inspection_details_gcws_type(self, value):
        self._input_inspection_details_gcws_type = value
        self.input_inspection_details_gcws_type_changed.emit(value)

    #input_inspection_details_grade_crossing_type
    @property
    def input_inspection_details_grade_crossing_type(self):
        return self._input_inspection_details_grade_crossing_type

    @input_inspection_details_grade_crossing_type.setter
    def input_inspection_details_grade_crossing_type(self, value):
        self._input_inspection_details_grade_crossing_type = value
        self.input_inspection_details_grade_crossing_type_changed.emit(value)

    #input_inspection_details_province = None
    #input_inspection_details_railway_authority = None
    #input_inspection_details_reason_for_assessment = None
    #input_inspection_details_road_authority = None
    #input_inspection_details_subdivision_name = None
    #input_inspection_details_track_type = None

    # COLLISION HISTORY (5 YEAR PERIOD)
    #Group TextEdits
    #input_collision_history_comments = None

    #Group LineEdits
    #input_collision_history_fatal_injury
    @property
    def input_collision_history_fatal_injury(self):
        return self.input_collision_history_fatal_injury

    @input_collision_history_fatal_injury.setter
    def input_collision_history_fatal_injury(self, value):
        self._input_collision_history_fatal_injury = value
        self.input_collision_history_fatal_injury_changed.emit(value)

    #input_collision_history_fatalities = None 
    #input_collision_history_personal_injuries = None
    
    #input_collision_history_personal_injury
    @property
    def input_collision_history_personal_injury(self):
        return self.input_collision_history_personal_injury

    @input_collision_history_personal_injury.setter
    def input_collision_history_personal_injury(self, value):
        self._input_collision_history_personal_injury = value
        self.input_collision_history_personal_injury_changed.emit(value)

    #input_collision_history_property_damage
    @property
    def input_collision_history_property_damage(self):
        return self.input_collision_history_property_damage

    @input_collision_history_property_damage.setter
    def input_collision_history_property_damage(self, value):
        self._input_collision_history_property_damage = value
        self.input_collision_history_property_damage_changed.emit(value)

    #Group Labels
    #input_collision_history_total_5_year_period
    @property
    def input_collision_history_total_5_year_period(self):
        return self.input_collision_history_total_5_year_period

    @input_collision_history_total_5_year_period.setter
    def input_collision_history_total_5_year_period(self, value):
        self._input_collision_history_total_5_year_period = value
        self.input_collision_history_total_5_year_period_changed.emit(value)

    # GENERAL INFORMATION
    #Group TextEdits
    #input_general_info_comments = None

    #Group LineEdits
    #input_general_info_observe_special_buildings = None 

    #input_general_info_rail_max_railway_operating_speed_freight
    @property
    def input_general_info_rail_max_railway_operating_speed_freight(self):
        return self.input_general_info_rail_max_railway_operating_speed_freight

    @input_general_info_rail_max_railway_operating_speed_freight.setter
    def input_general_info_rail_max_railway_operating_speed_freight(self, value):
        self._input_general_info_rail_max_railway_operating_speed_freight = value
        self.input_general_info_rail_max_railway_operating_speed_freight_changed.emit(value)

    #input_general_info_rail_max_railway_operating_speed_passenger
    @property
    def input_general_info_rail_max_railway_operating_speed_passenger(self):
        return self.input_general_info_rail_max_railway_operating_speed_passenger

    @input_general_info_rail_max_railway_operating_speed_passenger.setter
    def input_general_info_rail_max_railway_operating_speed_passenger(self, value):
        self._input_general_info_rail_max_railway_operating_speed_passenger = value
        self.input_general_info_rail_max_railway_operating_speed_passenger_changed.emit(value)

    #input_general_info_rail_no_trains_per_day_freight
    @property
    def input_general_info_rail_no_trains_per_day_freight(self):
        return self.input_general_info_rail_no_trains_per_day_freight

    @input_general_info_rail_no_trains_per_day_freight.setter
    def input_general_info_rail_no_trains_per_day_freight(self, value):
        self._input_general_info_rail_no_trains_per_day_freight = value
        self.input_general_info_rail_no_trains_per_day_freight_changed.emit(value)

    #input_general_info_rail_no_trains_per_day_passengers
    @property
    def input_general_info_rail_no_trains_per_day_passengers(self):
        return self.input_general_info_rail_no_trains_per_day_passengers

    @input_general_info_rail_no_trains_per_day_passengers.setter
    def input_general_info_rail_no_trains_per_day_passengers(self, value):
        self._input_general_info_rail_no_trains_per_day_passengers = value
        self.input_general_info_rail_no_trains_per_day_passengers_changed.emit(value)

    #input_general_info_rail_no_tracks_main
    @property
    def input_general_info_rail_no_tracks_main(self):
        return self.input_general_info_rail_no_tracks_main

    @input_general_info_rail_no_tracks_main.setter
    def input_general_info_rail_no_tracks_main(self, value):
        self._input_general_info_rail_no_tracks_main = value
        self.input_general_info_rail_no_tracks_main_changed.emit(value)

    #input_general_info_rail_no_tracks_other
    @property
    def input_general_info_rail_no_tracks_other(self):
        return self.input_general_info_rail_no_tracks_other

    @input_general_info_rail_no_tracks_other.setter
    def input_general_info_rail_no_tracks_other(self, value):
        self._input_general_info_rail_no_tracks_other = value
        self.input_general_info_rail_no_tracks_other_changed.emit(value)

    #input_general_info_rail_railway_design_speed
    @property
    def input_general_info_rail_railway_design_speed(self):
        return self.input_general_info_rail_railway_design_speed

    @input_general_info_rail_railway_design_speed.setter
    def input_general_info_rail_railway_design_speed(self, value):
        self._input_general_info_rail_railway_design_speed = value
        self.input_general_info_rail_railway_design_speed_changed.emit(value)
 
    #input_general_info_road_aadt_current
    @property
    def input_general_info_road_aadt_current(self):
        return self.input_general_info_road_aadt_current

    @input_general_info_road_aadt_current.setter
    def input_general_info_road_aadt_current(self, value):
        self._input_general_info_road_aadt_current = value
        self.input_general_info_road_aadt_current_changed.emit(value)
 
    #input_general_info_road_aadt_forecast
    @property
    def input_general_info_road_aadt_forecast(self):
        return self.input_general_info_road_aadt_forecast

    @input_general_info_road_aadt_forecast.setter
    def input_general_info_road_aadt_forecast(self, value):
        self._input_general_info_road_aadt_forecast = value
        self.input_general_info_road_aadt_forecast_changed.emit(value)
  
    #input_general_info_road_aadt_year_current = None 
    #input_general_info_road_aadt_year_forecasted = None 
    #input_general_info_road_cyclist_per_day = None

    #input_general_info_road_no_traffic_lanes_bidirectional
    @property
    def input_general_info_road_no_traffic_lanes_bidirectional(self):
        return self.input_general_info_road_no_traffic_lanes_bidirectional

    @input_general_info_road_no_traffic_lanes_bidirectional.setter
    def input_general_info_road_no_traffic_lanes_bidirectional(self, value):
        self._input_general_info_road_no_traffic_lanes_bidirectional = value
        self.input_general_info_road_no_traffic_lanes_bidirectional_changed.emit(value)
 
    #input_general_info_road_no_traffic_lanes_northbound_or_eastbound
    @property
    def input_general_info_road_no_traffic_lanes_northbound_or_eastbound(self):
        return self.input_general_info_road_no_traffic_lanes_northbound_or_eastbound

    @input_general_info_road_no_traffic_lanes_northbound_or_eastbound.setter
    def input_general_info_road_no_traffic_lanes_northbound_or_eastbound(self, value):
        self._input_general_info_road_no_traffic_lanes_northbound_or_eastbound = value
        self.input_general_info_road_no_traffic_lanes_northbound_or_eastbound_changed.emit(value)

    #input_general_info_road_no_traffic_lanes_southbound_or_westbound
    @property
    def input_general_info_road_no_traffic_lanes_southbound_or_westbound(self):
        return self.input_general_info_road_no_traffic_lanes_southbound_or_westbound

    @input_general_info_road_no_traffic_lanes_southbound_or_westbound.setter
    def input_general_info_road_no_traffic_lanes_southbound_or_westbound(self, value):
        self._input_general_info_road_no_traffic_lanes_southbound_or_westbound = value
        self.input_general_info_road_no_traffic_lanes_southbound_or_westbound_changed.emit(value)

    #input_general_info_road_other_users = None 
    #input_general_info_road_other_users_daily_users = None 
    #input_general_info_road_pedestrians_per_day = None 

    #input_general_info_road_speed_design
    @property
    def input_general_info_road_speed_design(self):
        return self.input_general_info_road_speed_design

    @input_general_info_road_speed_design.setter
    def input_general_info_road_speed_design(self, value):
        self._input_general_info_road_speed_design = value
        self.input_general_info_road_speed_design_changed.emit(value)
  
    #input_general_info_road_speed_posted = None 

    #Group ComboBoxes
    #input_general_info_observe_roadway_illumination = None
    #input_general_info_observe_surrounding_land_use = None
    #input_general_info_rail_train_switching = None        
    #input_general_info_road_assistive_pedestrian_devices = None

    #input_general_info_road_classification
    @property
    def input_general_info_road_classification(self):
        return self.input_general_info_road_classification

    @input_general_info_road_classification.setter
    def input_general_info_road_classification(self, value):
        self._input_general_info_road_classification = value
        self.input_general_info_road_classification_changed.emit(value)
            
    #input_general_info_road_dangerous_goods_route = None
    #input_general_info_road_school_bus_route = None
    #input_general_info_road_seasonal_volume_fluctuations = None

    #input_general_info_road_sidewalks
    @property
    def input_general_info_road_sidewalks(self):
        return self.input_general_info_road_sidewalks

    @input_general_info_road_sidewalks.setter
    def input_general_info_road_sidewalks(self, value):
        self._input_general_info_road_sidewalks = value
        self.input_general_info_road_sidewalks_changed.emit(value)

    #Group Labels
    #input_general_info_rail_no_tracks_total
    @property
    def input_general_info_rail_no_tracks_total(self):
        return self.input_general_info_rail_no_tracks_total

    @input_general_info_rail_no_tracks_total.setter
    def input_general_info_rail_no_tracks_total(self, value):
        self._input_general_info_rail_no_tracks_total = value
        self.input_general_info_rail_no_tracks_total_changed.emit(value)

    #input_general_info_rail_no_trains_per_day_total
    @property
    def input_general_info_rail_no_trains_per_day_total(self):
        return self.input_general_info_rail_no_trains_per_day_total

    @input_general_info_rail_no_trains_per_day_total.setter
    def input_general_info_rail_no_trains_per_day_total(self, value):
        self._input_general_info_rail_no_trains_per_day_total = value
        self.input_general_info_rail_no_trains_per_day_total_changed.emit(value)

    #input_general_info_road_no_traffic_lanes_total
    @property
    def input_general_info_road_no_traffic_lanes_total(self):
        return self.input_general_info_road_no_traffic_lanes_total

    @input_general_info_road_no_traffic_lanes_total.setter
    def input_general_info_road_no_traffic_lanes_total(self, value):
        self._input_general_info_road_no_traffic_lanes_total = value
        self.input_general_info_road_no_traffic_lanes_total_changed.emit(value)

    # DESIGN CONSIDERATIONS (GCS SECTION 10)
    #Group TextEdits
    #input_design_comments = None

    #Group LineEdits
    #input_design_measure_adjacent_track_clearance_distance
    @property
    def input_design_measure_adjacent_track_clearance_distance(self):
        return self.input_design_measure_adjacent_track_clearance_distance

    @input_design_measure_adjacent_track_clearance_distance.setter
    def input_design_measure_adjacent_track_clearance_distance(self, value):
        self._input_design_measure_adjacent_track_clearance_distance = value
        self.input_design_measure_adjacent_track_clearance_distance_changed.emit(value)

    #input_design_measure_adjacent_track_separation_distance
    @property
    def input_design_measure_adjacent_track_separation_distance(self):
        return self.input_design_measure_adjacent_track_separation_distance

    @input_design_measure_adjacent_track_separation_distance.setter
    def input_design_measure_adjacent_track_separation_distance(self, value):
        self._input_design_measure_adjacent_track_separation_distance = value
        self.input_design_measure_adjacent_track_separation_distance_changed.emit(value)

    #input_design_measure_clearance_distance_pedestrian
    @property
    def input_design_measure_clearance_distance_pedestrian(self):
        return self.input_design_measure_clearance_distance_pedestrian

    @input_design_measure_clearance_distance_pedestrian.setter
    def input_design_measure_clearance_distance_pedestrian(self, value):
        self._input_design_measure_clearance_distance_pedestrian = value
        self.input_design_measure_clearance_distance_pedestrian_changed.emit(value)

    #input_design_measure_clearance_distance_vehicle
    @property
    def input_design_measure_clearance_distance_vehicle(self):
        return self.input_design_measure_clearance_distance_vehicle

    @input_design_measure_clearance_distance_vehicle.setter
    def input_design_measure_clearance_distance_vehicle(self, value):
        self._input_design_measure_clearance_distance_vehicle = value
        self.input_design_measure_clearance_distance_vehicle_changed.emit(value)

    #input_design_road_max_approach_grade_within_s
    @property
    def input_design_road_max_approach_grade_within_s(self):
        return self.input_design_road_max_approach_grade_within_s

    @input_design_road_max_approach_grade_within_s.setter
    def input_design_road_max_approach_grade_within_s(self, value):
        self._input_design_road_max_approach_grade_within_s = value
        self.input_design_road_max_approach_grade_within_s_changed.emit(value)

    #Group ComboBoxes
    #input_design_observe_field_acceleration_times_exceed_td = None

    #input_design_road_design_vehicle_type
    @property
    def input_design_road_design_vehicle_type(self):
        return self.input_design_road_design_vehicle_type

    @input_design_road_design_vehicle_type.setter
    def input_design_road_design_vehicle_type(self, value):
        self._input_design_road_design_vehicle_type = value
        self.input_design_road_design_vehicle_type_changed.emit(value)

    #Group Labels
    #input_design_calculate_adjacent_track_clearance_time
    @property
    def input_design_calculate_adjacent_track_clearance_time(self):
        return self.input_design_calculate_adjacent_track_clearance_time

    @input_design_calculate_adjacent_track_clearance_time.setter
    def input_design_calculate_adjacent_track_clearance_time(self, value):
        self._input_design_calculate_adjacent_track_clearance_time = value
        self.input_design_calculate_adjacent_track_clearance_time_changed.emit(value)

    #input_design_calculate_clearance_time_crossing_pedestrian_design_check
    @property
    def input_design_calculate_clearance_time_crossing_pedestrian_design_check(self):
        return self.input_design_calculate_clearance_time_crossing_pedestrian_design_check

    @input_design_calculate_clearance_time_crossing_pedestrian_design_check.setter
    def input_design_calculate_clearance_time_crossing_pedestrian_design_check(self, value):
        self._input_design_calculate_clearance_time_crossing_pedestrian_design_check = value
        self.input_design_calculate_clearance_time_crossing_pedestrian_design_check_changed.emit(value)

    #input_design_calculate_clearance_time_crossing_vehicle_design_check
    @property
    def input_design_calculate_clearance_time_crossing_vehicle_design_check(self):
        return self.input_design_calculate_clearance_time_crossing_vehicle_design_check

    @input_design_calculate_clearance_time_crossing_vehicle_design_check.setter
    def input_design_calculate_clearance_time_crossing_vehicle_design_check(self, value):
        self._input_design_calculate_clearance_time_crossing_vehicle_design_check = value
        self.input_design_calculate_clearance_time_crossing_vehicle_design_check_changed.emit(value)

    #input_design_calculate_clearance_time_gate_arm_ssd
    @property
    def input_design_calculate_clearance_time_gate_arm_ssd(self):
        return self.input_design_calculate_clearance_time_gate_arm_ssd

    @input_design_calculate_clearance_time_gate_arm_ssd.setter
    def input_design_calculate_clearance_time_gate_arm_ssd(self, value):
        self._input_design_calculate_clearance_time_gate_arm_ssd = value
        self.input_design_calculate_clearance_time_gate_arm_ssd_changed.emit(value)

    #input_design_calculate_clearance_time_gate_arm_stop
    @property
    def input_design_calculate_clearance_time_gate_arm_stop(self):
        return self.input_design_calculate_clearance_time_gate_arm_stop

    @input_design_calculate_clearance_time_gate_arm_stop.setter
    def input_design_calculate_clearance_time_gate_arm_stop(self, value):
        self._input_design_calculate_clearance_time_gate_arm_stop = value
        self.input_design_calculate_clearance_time_gate_arm_stop_changed.emit(value)

    #input_design_calculate_vehicle_travel_distance
    @property
    def input_design_calculate_vehicle_travel_distance(self):
        return self.input_design_calculate_vehicle_travel_distance

    @input_design_calculate_vehicle_travel_distance.setter
    def input_design_calculate_vehicle_travel_distance(self, value):
        self._input_design_calculate_vehicle_travel_distance = value
        self.input_design_calculate_vehicle_travel_distance_changed.emit(value)

    #input_design_input_reaction_time
    @property
    def input_design_input_reaction_time(self):
        return self.input_design_input_reaction_time

    @input_design_input_reaction_time.setter
    def input_design_input_reaction_time(self, value):
        self._input_design_input_reaction_time = value
        self.input_design_input_reaction_time_changed.emit(value)

    #input_design_lookup_design_vehicle_class
    @property
    def input_design_lookup_design_vehicle_class(self):
        return self.input_design_lookup_design_vehicle_class

    @input_design_lookup_design_vehicle_class.setter
    def input_design_lookup_design_vehicle_class(self, value):
        self._input_design_lookup_design_vehicle_class = value
        self.input_design_lookup_design_vehicle_class_changed.emit(value)

    #input_design_lookup_design_vehicle_length
    @property
    def input_design_lookup_design_vehicle_length(self):
        return self.input_design_lookup_design_vehicle_length

    @input_design_lookup_design_vehicle_length.setter
    def input_design_lookup_design_vehicle_length(self, value):
        self._input_design_lookup_design_vehicle_length = value
        self.input_design_lookup_design_vehicle_length_changed.emit(value)

    #input_design_lookup_grade_adjustment_factor
    @property
    def input_design_lookup_grade_adjustment_factor(self):
        return self.input_design_lookup_grade_adjustment_factor

    @input_design_lookup_grade_adjustment_factor.setter
    def input_design_lookup_grade_adjustment_factor(self, value):
        self._input_design_lookup_grade_adjustment_factor = value
        self.input_design_lookup_grade_adjustment_factor_changed.emit(value)

    #input_design_lookup_vehicle_departure_time_crossing
    @property
    def input_design_lookup_vehicle_departure_time_crossing(self):
        return self.input_design_lookup_vehicle_departure_time_crossing

    @input_design_lookup_vehicle_departure_time_crossing.setter
    def input_design_lookup_vehicle_departure_time_crossing(self, value):
        self._input_design_lookup_vehicle_departure_time_crossing = value
        self.input_design_lookup_vehicle_departure_time_crossing_changed.emit(value)

    #input_design_lookup_vehicle_departure_time_gate_arm_clearance
    @property
    def input_design_lookup_vehicle_departure_time_gate_arm_clearance(self):
        return self.input_design_lookup_vehicle_departure_time_gate_arm_clearance

    @input_design_lookup_vehicle_departure_time_gate_arm_clearance.setter
    def input_design_lookup_vehicle_departure_time_gate_arm_clearance(self, value):
        self._input_design_lookup_vehicle_departure_time_gate_arm_clearance = value
        self.input_design_lookup_vehicle_departure_time_gate_arm_clearance_changed.emit(value)
    
    # LOCATION OF GRADE CROSSING (GCS SECTION 11)
    #Group TextEdits
    #input_location_of_grade_crossing_comments = None

    #Group LineEdits
    #input_location_of_grade_crossing_nearest_intersection_other_n_or_e_approach = None 
    #input_location_of_grade_crossing_nearest_intersection_other_s_of_w_approach = None 
    
    #input_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach
    @property
    def input_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach(self):
        return self.input_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach

    @input_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach.setter
    def input_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach(self, value):
        self._input_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach = value
        self.input_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach_changed.emit(value)

    #input_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach
    @property
    def input_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach(self):
        return self.input_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach

    @input_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach.setter
    def input_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach(self, value):
        self._input_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach = value
        self.input_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach_changed.emit(value)
  
    #input_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach
    @property
    def input_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach(self):
        return self.input_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach

    @input_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach.setter
    def input_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach(self, value):
        self._input_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach = value
        self.input_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach_changed.emit(value)

    #input_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach
    @property
    def input_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach(self):
        return self.input_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach

    @input_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach.setter
    def input_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach(self, value):
        self._input_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach = value
        self.input_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach_changed.emit(value)

    #group ComboBoxes
    #input_location_of_grade_crossing_observe_nearby_pedestrian_crosswalk = None
    #input_location_of_grade_crossing_queue_condition = None
    #input_location_of_grade_crossing_visibility_of_warning_lights = None
    
    # GRADE CROSSING SURFACE (GCS SECTION 5)
    #Group TextEdits
    #input_grade_crossing_surface_comments = None

    #Group LineEdits
    #input_grade_crossing_surface_measure_crossing_surface_extension_n_or_e_approach = None 
    #input_grade_crossing_surface_measure_crossing_surface_extension_s_or_w_approach = None 
    #input_grade_crossing_surface_measure_crossing_surface_width = None 
    #input_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_n_or_e_approach = None 
    #input_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_s_or_w_approach = None 
    #input_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_n_or_e_approach = None 
    #input_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_s_or_w_approach = None 
    #input_grade_crossing_surface_measure_elevation_top_of_rail_above_road_surface = None 
    #input_grade_crossing_surface_measure_elevation_top_of_rail_below_road_surface = None 
    #input_grade_crossing_surface_measure_flangeway_depth = None 
    #input_grade_crossing_surface_measure_flangeway_width = None 
    #input_grade_crossing_surface_measure_road_surface_median_width = None 
    #input_grade_crossing_surface_measure_road_surface_shoulder_n_or_e_approach = None 
    #input_grade_crossing_surface_measure_road_surface_shoulder_s_or_w_approach = None 
    #input_grade_crossing_surface_measure_road_surface_travel_lanes_width_n_or_e_approach = None 
    #input_grade_crossing_surface_measure_road_surface_travel_lanes_width_s_or_w_approach = None 
    #input_grade_crossing_surface_measure_side_grinding_depth = None 
    #input_grade_crossing_surface_measure_side_grinding_width = None 
    #input_grade_crossing_surface_measure_sidewalk_extension_n_or_e_approach = None 
    #input_grade_crossing_surface_measure_sidewalk_extension_s_or_w_approach = None 
    #input_grade_crossing_surface_measure_sidewalk_width_n_or_e_approach = None 
    #input_grade_crossing_surface_measure_sidewalk_width_s_or_w_approach = None 

    #Group ComboBoxes
    #input_grade_crossing_surface_observe_crossing_smoothness = None
    #input_grade_crossing_surface_observe_crossing_surface_condition = None
    #input_grade_crossing_surface_observe_material = None
    #input_grade_crossing_surface_observe_road_approach_surface_condition = None
    #input_grade_crossing_surface_observe_road_approach_surface_type = None

    # ROAD GEOMETRY (GCS SECTION 6)
    #Group TextEdits 
    #input_road_geometry_comments = None

    #Group LineEdits
    #input_road_geometry_measure_railway_cross_slope
    @property
    def input_road_geometry_measure_railway_cross_slope(self):
        return self.input_road_geometry_measure_railway_cross_slope

    @input_road_geometry_measure_railway_cross_slope.setter
    def input_road_geometry_measure_railway_cross_slope(self, value):
        self._input_road_geometry_measure_railway_cross_slope = value
        self.input_road_geometry_measure_railway_cross_slope_changed.emit(value)
 
    #input_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_n_or_e_approach = None 
    #input_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_s_or_w_approach = None 
    #input_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_n_or_e_approach = None 
    #input_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_s_or_w_approach = None 

    #input_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach
    @property
    def input_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach(self):
        return self.input_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach

    @input_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach.setter
    def input_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach(self, value):
        self._input_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach = value
        self.input_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach_changed.emit(value)

    #input_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach
    @property
    def input_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach(self):
        return self.input_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach

    @input_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach.setter
    def input_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach(self, value):
        self._input_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach = value
        self.input_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach_changed.emit(value)

    #input_road_geometry_rail_superelevation_n_or_e_approach
    @property
    def input_road_geometry_rail_superelevation_n_or_e_approach(self):
        return self.input_road_geometry_rail_superelevation_n_or_e_approach

    @input_road_geometry_rail_superelevation_n_or_e_approach.setter
    def input_road_geometry_rail_superelevation_n_or_e_approach(self, value):
        self._input_road_geometry_rail_superelevation_n_or_e_approach = value
        self.input_road_geometry_rail_superelevation_n_or_e_approach_changed.emit(value)

    #input_road_geometry_rail_superelevation_s_or_w_approach
    @property
    def input_road_geometry_rail_superelevation_s_or_w_approach(self):
        return self.input_road_geometry_rail_superelevation_s_or_w_approach

    @input_road_geometry_rail_superelevation_s_or_w_approach.setter
    def input_road_geometry_rail_superelevation_s_or_w_approach(self, value):
        self._input_road_geometry_rail_superelevation_s_or_w_approach = value
        self.input_road_geometry_rail_superelevation_s_or_w_approach_changed.emit(value)
        
    #input_road_geometry_road_crossing_angle = None 
    
    #input_road_geometry_road_general_approach_grade_n_or_e_approach
    @property
    def input_road_geometry_road_general_approach_grade_n_or_e_approach(self):
        return self.input_road_geometry_road_general_approach_grade_n_or_e_approach

    @input_road_geometry_road_general_approach_grade_n_or_e_approach.setter
    def input_road_geometry_road_general_approach_grade_n_or_e_approach(self, value):
        self._input_road_geometry_road_general_approach_grade_n_or_e_approach = value
        self.input_road_geometry_road_general_approach_grade_n_or_e_approach_changed.emit(value)

    #input_road_geometry_road_general_approach_grade_s_or_w_approach
    @property
    def input_road_geometry_road_general_approach_grade_s_or_w_approach(self):
        return self.input_road_geometry_road_general_approach_grade_s_or_w_approach

    @input_road_geometry_road_general_approach_grade_s_or_w_approach.setter
    def input_road_geometry_road_general_approach_grade_s_or_w_approach(self, value):
        self._input_road_geometry_road_general_approach_grade_s_or_w_approach = value
        self.input_road_geometry_road_general_approach_grade_s_or_w_approach_changed.emit(value)

    #Group ComboBoxes
    #input_road_geometry_observe_lane_width_crossing_vs_approach_n_or_e_approach = None
    #input_road_geometry_observe_lane_width_crossing_vs_approach_s_or_w_approach = None
    #input_road_geometry_observe_low_bed_truck_condition = None
    #input_road_geometry_observe_smooth_alignment_within_ssd_n_or_e_approach = None
    #input_road_geometry_observe_smooth_alignment_within_ssd_s_or_w_approach = None
    
    #Group Labels
    #input_road_geometry_lookup_gradient_difference
    @property
    def input_road_geometry_lookup_gradient_difference(self):
        return self.input_road_geometry_lookup_gradient_difference

    @input_road_geometry_lookup_gradient_difference.setter
    def input_road_geometry_lookup_gradient_difference(self, value):
        self._input_road_geometry_lookup_gradient_difference = value
        self.input_road_geometry_lookup_gradient_difference_changed.emit(value)
    
    # SIGHTLINES (GCS SECTION 7)
    #Group TextEdits
    #input_sightlines_comments = None
    
    #Group LineEdits
    #input_sightlines_measure_dssd_actual_n_or_e_approach_left = None 
    #input_sightlines_measure_dssd_actual_n_or_e_approach_right = None 
    #input_sightlines_measure_dssd_actual_s_or_w_approach_left = None 
    #input_sightlines_measure_dssd_actual_s_or_w_approach_right = None 
    #input_sightlines_measure_dstopped_actual_n_or_e_approach_driver_left = None 
    #input_sightlines_measure_dstopped_actual_n_or_e_approach_driver_right = None 
    #input_sightlines_measure_dstopped_actual_s_or_w_approach_driver_left = None 
    #input_sightlines_measure_dstopped_actual_s_or_w_approach_driver_right = None 
    #input_sightlines_measure_ssd_actual_n_or_e_approach = None 
    #input_sightlines_measure_ssd_actual_s_or_w_approach = None 

    #Group ComboBoxes
    #input_sightlines_observe_sightline_obstructions = None

    #Group Labels
    #input_sightlines_calculate_dssd_vehicle_min_ft
    @property
    def input_sightlines_calculate_dssd_vehicle_min_ft(self):
        return self.input_sightlines_calculate_dssd_vehicle_min_ft

    @input_sightlines_calculate_dssd_vehicle_min_ft.setter
    def input_sightlines_calculate_dssd_vehicle_min_ft(self, value):
        self._input_sightlines_calculate_dssd_vehicle_min_ft = value
        self.input_sightlines_calculate_dssd_vehicle_min_ft_changed.emit(value)

    #input_sightlines_calculate_dssd_vehicle_min_m
    @property
    def input_sightlines_calculate_dssd_vehicle_min_m(self):
        return self.input_sightlines_calculate_dssd_vehicle_min_m

    @input_sightlines_calculate_dssd_vehicle_min_m.setter
    def input_sightlines_calculate_dssd_vehicle_min_m(self, value):
        self._input_sightlines_calculate_dssd_vehicle_min_m = value
        self.input_sightlines_calculate_dssd_vehicle_min_m_changed.emit(value)

    #input_sightlines_calculate_dstopped_pedestrian_min_ft
    @property
    def input_sightlines_calculate_dstopped_pedestrian_min_ft(self):
        return self.input_sightlines_calculate_dstopped_pedestrian_min_ft

    @input_sightlines_calculate_dstopped_pedestrian_min_ft.setter
    def input_sightlines_calculate_dstopped_pedestrian_min_ft(self, value):
        self._input_sightlines_calculate_dstopped_pedestrian_min_ft = value
        self.input_sightlines_calculate_dstopped_pedestrian_min_ft_changed.emit(value)

    #input_sightlines_calculate_dstopped_pedestrian_min_m
    @property
    def input_sightlines_calculate_dstopped_pedestrian_min_m(self):
        return self.input_sightlines_calculate_dstopped_pedestrian_min_m

    @input_sightlines_calculate_dstopped_pedestrian_min_m.setter
    def input_sightlines_calculate_dstopped_pedestrian_min_m(self, value):
        self._input_sightlines_calculate_dstopped_pedestrian_min_m = value
        self.input_sightlines_calculate_dstopped_pedestrian_min_m_changed.emit(value)

    #input_sightlines_calculate_dstopped_vehicle_min_ft
    @property
    def input_sightlines_calculate_dstopped_vehicle_min_ft(self):
        return self.input_sightlines_calculate_dstopped_vehicle_min_ft

    @input_sightlines_calculate_dstopped_vehicle_min_ft.setter
    def input_sightlines_calculate_dstopped_vehicle_min_ft(self, value):
        self._input_sightlines_calculate_dstopped_vehicle_min_ft = value
        self.input_sightlines_calculate_dstopped_vehicle_min_ft_changed.emit(value)

    #input_sightlines_calculate_dstopped_vehicle_min_m
    @property
    def input_sightlines_calculate_dstopped_vehicle_min_m(self):
        return self.input_sightlines_calculate_dstopped_vehicle_min_m

    @input_sightlines_calculate_dstopped_vehicle_min_m.setter
    def input_sightlines_calculate_dstopped_vehicle_min_m(self, value):
        self._input_sightlines_calculate_dstopped_vehicle_min_m = value
        self.input_sightlines_calculate_dstopped_vehicle_min_m_changed.emit(value)

    #input_sightlines_lookup_ssd_minimum_n_or_e_approach
    @property
    def input_sightlines_lookup_ssd_minimum_n_or_e_approach(self):
        return self.input_sightlines_lookup_ssd_minimum_n_or_e_approach

    @input_sightlines_lookup_ssd_minimum_n_or_e_approach.setter
    def input_sightlines_lookup_ssd_minimum_n_or_e_approach(self, value):
        self._input_sightlines_lookup_ssd_minimum_n_or_e_approach = value
        self.input_sightlines_lookup_ssd_minimum_n_or_e_approach_changed.emit(value)

    #input_sightlines_lookup_ssd_minimum_s_or_w_approach
    @property
    def input_sightlines_lookup_ssd_minimum_s_or_w_approach(self):
        return self.input_sightlines_lookup_ssd_minimum_s_or_w_approach

    @input_sightlines_lookup_ssd_minimum_s_or_w_approach.setter
    def input_sightlines_lookup_ssd_minimum_s_or_w_approach(self, value):
        self._input_sightlines_lookup_ssd_minimum_s_or_w_approach = value
        self.input_sightlines_lookup_ssd_minimum_s_or_w_approach_changed.emit(value)

    # SIGNS AND PAVEMENT MARKINGS (GCS SECTION 8)
    #Group TextEdits
    #DELETE input_signs_and_markings_advisory_speed_comments = None
    #DELETE input_signs_and_markings_comments = None
    #DELETE input_signs_and_markings_emergency_notification_comments = None
    #DELETE input_signs_and_markings_number_of_tracks_comments = None
    #DELETE input_signs_and_markings_railway_crossing_ahead_comments = None
    #DELETE input_signs_and_markings_railway_crossing_comments = None
    #DELETE input_signs_and_markings_stop_comments = None
    #DELETE input_signs_and_markings_stop_sign_ahead_comments = None

    #Group LineEdits
    #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_rail = None 
    #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_road = None 
    #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_height = None 
    #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_rail = None 
    #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_road = None 
    #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_height = None 
    #input_signs_and_markings_stop_n_or_e_approach_height = None 
    #input_signs_and_markings_stop_n_or_e_approach_location_from_rail = None 
    #input_signs_and_markings_stop_n_or_e_approach_location_from_road = None 
    #input_signs_and_markings_stop_s_or_w_approach_height = None 
    #input_signs_and_markings_stop_s_or_w_approach_location_from_rail = None 
    #input_signs_and_markings_stop_s_or_w_approach_location_from_road = None 
    #input_signs_and_markings_stop_sign_ahead_n_or_e_approach_height = None 
    #input_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_rail = None 
    #input_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_road = None 
    #input_signs_and_markings_stop_sign_ahead_s_or_w_approach_height = None 
    #input_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_rail = None 
    #input_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_road = None 

    #Group ComboBoxes
    #input_signs_and_markings_advisory_speed_n_or_e_approach_present = None
    #input_signs_and_markings_advisory_speed_n_or_e_approach_with_wa_18_20 = None
    #input_signs_and_markings_advisory_speed_s_or_w_approach_present = None
    #input_signs_and_markings_advisory_speed_s_or_w_approach_with_wa_18_20 = None
    #input_signs_and_markings_dividing_lines_present = None
    #input_signs_and_markings_emergency_notification_n_or_e_approach_condition = None
    #input_signs_and_markings_emergency_notification_n_or_e_approach_legible = None
    #input_signs_and_markings_emergency_Notification_n_or_e_approach_orientation = None
    #input_signs_and_markings_emergency_notification_n_or_e_approach_present = None
    #input_signs_and_markings_emergency_notification_s_or_w_approach_condition = None
    #input_signs_and_markings_emergency_notification_s_or_w_approach_legible = None
    #input_signs_and_markings_emergency_notification_s_or_w_approach_orientation = None
    #input_signs_and_markings_emergency_notification_s_or_w_approach_present = None
    #input_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_1b = None
    #input_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_3c = None
    #input_signs_and_markings_number_of_tracks_n_or_e_approach_present = None
    #input_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_1b = None
    #input_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_3c = None
    #input_signs_and_markings_number_of_tracks_s_or_w_approach_present = None
    #input_signs_and_markings_per_mutcd = None
    #input_signs_and_markings_posted_speed_n_or_e_approach_present = None
    #input_signs_and_markings_posted_speed_s_or_w_approach_present = None
    #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_orientation = None
    #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_present = None
    #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_orientation = None
    #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_present = None
    #input_signs_and_markings_railway_crossing_n_or_e_approach_per_fig_8_1a = None
    #input_signs_and_markings_railway_crossing_n_or_e_approach_present = None
    #input_signs_and_markings_railway_crossing_s_or_w_approach_per_fig_8_1a = None
    #input_signs_and_markings_railway_crossing_s_or_w_approach_present = None
    #input_signs_and_markings_sidewalks_present = None
    #input_signs_and_markings_stop_n_or_e_approach_per_fig_8_4 = None
    #input_signs_and_markings_stop_n_or_e_approach_present = None
    #input_signs_and_markings_stop_n_or_e_approach_same_post = None
    #input_signs_and_markings_stop_s_or_w_approach_per_fig_8_4 = None
    #input_signs_and_markings_stop_s_or_w_approach_present = None
    #input_signs_and_markings_stop_s_or_w_approach_same_post = None
    #input_signs_and_markings_stop_sign_ahead_n_or_e_approach_present = None
    #input_signs_and_markings_stop_sign_ahead_s_or_w_approach_present = None

    # GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)
    # Group Labels
    #input_gcws_warrant_private_9_3
    @property
    def input_gcws_warrant_private_9_3(self):
        return self.input_gcws_warrant_private_9_3

    @input_gcws_warrant_private_9_3.setter
    def input_gcws_warrant_private_9_3(self, value):
        self._input_gcws_warrant_private_9_3 = value
        self.input_gcws_warrant_private_9_3_changed.emit(value)

    #input_gcws_warrant_private_9_3_1
    @property
    def input_gcws_warrant_private_9_3_1(self):
        return self.input_gcws_warrant_private_9_3_1

    @input_gcws_warrant_private_9_3_1.setter
    def input_gcws_warrant_private_9_3_1(self, value):
        self._input_gcws_warrant_private_9_3_1 = value
        self.input_gcws_warrant_private_9_3_1_changed.emit(value)

    #input_gcws_warrant_private_9_3_2_a
    @property
    def input_gcws_warrant_private_9_3_2_a(self):
        return self.input_gcws_warrant_private_9_3_2_a

    @input_gcws_warrant_private_9_3_2_a.setter
    def input_gcws_warrant_private_9_3_2_a(self, value):
        self._input_gcws_warrant_private_9_3_2_a = value
        self.input_gcws_warrant_private_9_3_2_a_changed.emit(value)

    #input_gcws_warrant_private_9_3_2_b
    @property
    def input_gcws_warrant_private_9_3_2_b(self):
        return self.input_gcws_warrant_private_9_3_2_b

    @input_gcws_warrant_private_9_3_2_b.setter
    def input_gcws_warrant_private_9_3_2_b(self, value):
        self._input_gcws_warrant_private_9_3_2_b = value
        self.input_gcws_warrant_private_9_3_2_b_changed.emit(value)

    #input_gcws_warrant_private_9_3_2_c
    @property
    def input_gcws_warrant_private_9_3_2_c(self):
        return self.input_gcws_warrant_private_9_3_2_c

    @input_gcws_warrant_private_9_3_2_c.setter
    def input_gcws_warrant_private_9_3_2_c(self, value):
        self._input_gcws_warrant_private_9_3_2_c = value
        self.input_gcws_warrant_private_9_3_2_c_changed.emit(value)

    #input_gcws_warrant_public_9_1
    @property
    def input_gcws_warrant_public_9_1(self):
        return self.input_gcws_warrant_public_9_1

    @input_gcws_warrant_public_9_1.setter
    def input_gcws_warrant_public_9_1(self, value):
        self._input_gcws_warrant_public_9_1 = value
        self.input_gcws_warrant_public_9_1_changed.emit(value)

    #input_gcws_warrant_public_9_1_a
    @property
    def input_gcws_warrant_public_9_1_a(self):
        return self.input_gcws_warrant_public_9_1_a

    @input_gcws_warrant_public_9_1_a.setter
    def input_gcws_warrant_public_9_1_a(self, value):
        self._input_gcws_warrant_public_9_1_a = value
        self.input_gcws_warrant_public_9_1_a_changed.emit(value)

    #input_gcws_warrant_public_9_1_b
    @property
    def input_gcws_warrant_public_9_1_b(self):
        return self.input_gcws_warrant_public_9_1_b

    @input_gcws_warrant_public_9_1_b.setter
    def input_gcws_warrant_public_9_1_b(self, value):
        self._input_gcws_warrant_public_9_1_b = value
        self.input_gcws_warrant_public_9_1_b_changed.emit(value)

    #input_gcws_warrant_public_9_1_c
    @property
    def input_gcws_warrant_public_9_1_c(self):
        return self.input_gcws_warrant_public_9_1_c

    @input_gcws_warrant_public_9_1_c.setter
    def input_gcws_warrant_public_9_1_c(self, value):
        self._input_gcws_warrant_public_9_1_c = value
        self.input_gcws_warrant_public_9_1_c_changed.emit(value)

    #input_gcws_warrant_public_9_1_d_i
    @property
    def input_gcws_warrant_public_9_1_d_i(self):
        return self.input_gcws_warrant_public_9_1_d_i

    @input_gcws_warrant_public_9_1_d_i.setter
    def input_gcws_warrant_public_9_1_d_i(self, value):
        self._input_gcws_warrant_public_9_1_d_i = value
        self.input_gcws_warrant_public_9_1_d_i_changed.emit(value)

    #input_gcws_warrant_public_9_1_d_ii
    @property
    def input_gcws_warrant_public_9_1_d_ii(self):
        return self.input_gcws_warrant_public_9_1_d_ii

    @input_gcws_warrant_public_9_1_d_ii.setter
    def input_gcws_warrant_public_9_1_d_ii(self, value):
        self._input_gcws_warrant_public_9_1_d_ii = value
        self.input_gcws_warrant_public_9_1_d_ii_changed.emit(value)

    #input_gcws_warrant_public_9_1_d_iii
    @property
    def input_gcws_warrant_public_9_1_d_iii(self):
        return self.input_gcws_warrant_public_9_1_d_iii

    @input_gcws_warrant_public_9_1_d_iii.setter
    def input_gcws_warrant_public_9_1_d_iii(self, value):
        self._input_gcws_warrant_public_9_1_d_iii = value
        self.input_gcws_warrant_public_9_1_d_iii_changed.emit(value)

    #input_gcws_warrant_sidewalk_9_5
    @property
    def input_gcws_warrant_sidewalk_9_5(self):
        return self.input_gcws_warrant_sidewalk_9_5

    @input_gcws_warrant_sidewalk_9_5.setter
    def input_gcws_warrant_sidewalk_9_5(self, value):
        self._input_gcws_warrant_sidewalk_9_5 = value
        self.input_gcws_warrant_sidewalk_9_5_changed.emit(value)

    #input_gates_gcws_warrant_private_9_4_1_a
    @property
    def input_gates_gcws_warrant_private_9_4_1_a(self):
        return self.input_gates_gcws_warrant_private_9_4_1_a

    @input_gates_gcws_warrant_private_9_4_1_a.setter
    def input_gates_gcws_warrant_private_9_4_1_a(self, value):
        self._input_gates_gcws_warrant_private_9_4_1_a = value
        self.input_gates_gcws_warrant_private_9_4_1_a_changed.emit(value)

    #input_gates_gcws_warrant_private_9_4_1_b
    @property
    def input_gates_gcws_warrant_private_9_4_1_b(self):
        return self.input_gates_gcws_warrant_private_9_4_1_b

    @input_gates_gcws_warrant_private_9_4_1_b.setter
    def input_gates_gcws_warrant_private_9_4_1_b(self, value):
        self._input_gates_gcws_warrant_private_9_4_1_b = value
        self.input_gates_gcws_warrant_private_9_4_1_b_changed.emit(value)

    #input_gates_gcws_warrant_private_9_4_1_c
    @property
    def input_gates_gcws_warrant_private_9_4_1_c(self):
        return self.input_gates_gcws_warrant_private_9_4_1_c

    @input_gates_gcws_warrant_private_9_4_1_c.setter
    def input_gates_gcws_warrant_private_9_4_1_c(self, value):
        self._input_gates_gcws_warrant_private_9_4_1_c = value
        self.input_gates_gcws_warrant_private_9_4_1_c_changed.emit(value)

    #input_gates_gcws_warrant_public_9_2_1_a
    @property
    def input_gates_gcws_warrant_public_9_2_1_a(self):
        return self.input_gates_gcws_warrant_public_9_2_1_a

    @input_gates_gcws_warrant_public_9_2_1_a.setter
    def input_gates_gcws_warrant_public_9_2_1_a(self, value):
        self._input_gates_gcws_warrant_public_9_2_1_a = value
        self.input_gates_gcws_warrant_public_9_2_1_a_changed.emit(value)

    #input_gates_gcws_warrant_public_9_2_1_b
    @property
    def input_gates_gcws_warrant_public_9_2_1_b(self):
        return self.input_gates_gcws_warrant_public_9_2_1_b

    @input_gates_gcws_warrant_public_9_2_1_b.setter
    def input_gates_gcws_warrant_public_9_2_1_b(self, value):
        self._input_gates_gcws_warrant_public_9_2_1_b = value
        self.input_gates_gcws_warrant_public_9_2_1_b_changed.emit(value)

    #input_gates_gcws_warrant_public_9_2_1_c
    @property
    def input_gates_gcws_warrant_public_9_2_1_c(self):
        return self.input_gates_gcws_warrant_public_9_2_1_c

    @input_gates_gcws_warrant_public_9_2_1_c.setter
    def input_gates_gcws_warrant_public_9_2_1_c(self, value):
        self._input_gates_gcws_warrant_public_9_2_1_c = value
        self.input_gates_gcws_warrant_public_9_2_1_c_changed.emit(value)

    #input_gates_gcws_warrant_public_9_2_1_d
    @property
    def input_gates_gcws_warrant_public_9_2_1_d(self):
        return self.input_gates_gcws_warrant_public_9_2_1_d

    @input_gates_gcws_warrant_public_9_2_1_d.setter
    def input_gates_gcws_warrant_public_9_2_1_d(self, value):
        self._input_gates_gcws_warrant_public_9_2_1_d = value
        self.input_gates_gcws_warrant_public_9_2_1_d_changed.emit(value)

    #input_gates_gcws_warrant_public_9_2_1_e
    @property
    def input_gates_gcws_warrant_public_9_2_1_e(self):
        return self.input_gates_gcws_warrant_public_9_2_1_e

    @input_gates_gcws_warrant_public_9_2_1_e.setter
    def input_gates_gcws_warrant_public_9_2_1_e(self, value):
        self._input_gates_gcws_warrant_public_9_2_1_e = value
        self.input_gates_gcws_warrant_public_9_2_1_e_changed.emit(value)

    #input_gates_gcws_warrant_sidewalk_9_6
    @property
    def input_gates_gcws_warrant_sidewalk_9_6(self):
        return self.input_gates_gcws_warrant_sidewalk_9_6

    @input_gates_gcws_warrant_sidewalk_9_6.setter
    def input_gates_gcws_warrant_sidewalk_9_6(self, value):
        self._input_gates_gcws_warrant_sidewalk_9_6 = value
        self.input_gates_gcws_warrant_sidewalk_9_6_changed.emit(value)

    #input_gcws_warrants_comments = None

    # GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)
    #Group TextEdits
    #input_gcws_comments = None
        
    #Group LineEdits
    #input_gcws_measure_warning_device_n_or_e_approach_distance_from_rail = None 
    #input_gcws_measure_warning_device_n_or_e_approach_distance_from_road = None 
    #input_gcws_measure_warning_device_n_or_e_approach_distance_top_of_foundation = None 
    #input_gcws_measure_warning_device_n_or_e_approach_slope_from_foundation = None 
    #input_gcws_measure_warning_device_s_or_w_approach_distance_from_rail = None 
    #input_gcws_measure_warning_device_s_or_w_approach_distance_from_road = None 
    #input_gcws_measure_warning_device_s_or_w_approach_distance_top_of_foundation = None 
    #input_gcws_measure_warning_device_s_or_w_approach_slope_from_foundation = None 
    #input_gcws_rail_crossing_warning_time_actual = None 

    #Group ComboBox
    #input_gcws_observe_bell_if_sidewalk = None
    #input_gcws_observe_bells_condition = None
    #input_gcws_observe_bells_n_or_e_approach = None
    #input_gcws_observe_bells_s_or_w_approach = None
    #input_gcws_observe_cantilever_lights_condition = None
    #input_gcws_observe_cantilever_lights_n_or_e_approach = None
    #input_gcws_observe_cantilever_lights_s_or_w_approach = None
    #input_gcws_observe_gates_condition = None
    #input_gcws_observe_gates_n_or_e_approach = None
    #input_gcws_observe_gates_s_or_w_approach = None
    #input_gcws_observe_gcws_limited_use_with_walk_light_assembly = None
    #input_gcws_observe_gcws_limited_use_without_walk_light_assembly = None
    #input_gcws_observe_light_units_condition = None
    #input_gcws_observe_light_units_n_or_e_approach = None
    #input_gcws_observe_light_units_s_or_w_approach = None
    #input_gcws_observe_warning_time_consistency = None   
    #input_gcws_observe_warning_time_consistency_reduced_speed = None
    #input_gcws_rail_cut_out_circuit_requirements = None
    #input_gcws_rail_directional_stick_circuit_requirements = None
    #input_gcws_rail_self_diagnostic = None

    #Group Labels
    #input_gcws_rail_design_approach_warning_time
    @property
    def input_gcws_rail_design_approach_warning_time(self):
        return self.input_gcws_rail_design_approach_warning_time

    @input_gcws_rail_design_approach_warning_time.setter
    def input_gcws_rail_design_approach_warning_time(self, value):
        self._input_gcws_rail_design_approach_warning_time = value
        self.input_gcws_rail_design_approach_warning_time_changed.emit(value)

    #input_gcws_rail_design_warning_time_adjacent_crossing
    @property
    def input_gcws_rail_design_warning_time_adjacent_crossing(self):
        return self.input_gcws_rail_design_warning_time_adjacent_crossing

    @input_gcws_rail_design_warning_time_adjacent_crossing.setter
    def input_gcws_rail_design_warning_time_adjacent_crossing(self, value):
        self._input_gcws_rail_design_warning_time_adjacent_crossing = value
        self.input_gcws_rail_design_warning_time_adjacent_crossing_changed.emit(value)

    #input_gcws_rail_design_warning_time_clearance_distance
    @property
    def input_gcws_rail_design_warning_time_clearance_distance(self):
        return self.input_gcws_rail_design_warning_time_clearance_distance

    @input_gcws_rail_design_warning_time_clearance_distance.setter
    def input_gcws_rail_design_warning_time_clearance_distance(self, value):
        self._input_gcws_rail_design_warning_time_clearance_distance = value
        self.input_gcws_rail_design_warning_time_clearance_distance_changed.emit(value)

    #input_gcws_rail_design_warning_time_departure_time_pedestrian
    @property
    def input_gcws_rail_design_warning_time_departure_time_pedestrian(self):
        return self.input_gcws_rail_design_warning_time_departure_time_pedestrian

    @input_gcws_rail_design_warning_time_departure_time_pedestrian.setter
    def input_gcws_rail_design_warning_time_departure_time_pedestrian(self, value):
        self._input_gcws_rail_design_warning_time_departure_time_pedestrian = value
        self.input_gcws_rail_design_warning_time_departure_time_pedestrian_changed.emit(value)

    #input_gcws_rail_design_warning_time_departure_time_vehicle
    @property
    def input_gcws_rail_design_warning_time_departure_time_vehicle(self):
        return self.input_gcws_rail_design_warning_time_departure_time_vehicle

    @input_gcws_rail_design_warning_time_departure_time_vehicle.setter
    def input_gcws_rail_design_warning_time_departure_time_vehicle(self, value):
        self._input_gcws_rail_design_warning_time_departure_time_vehicle = value
        self.input_gcws_rail_design_warning_time_departure_time_vehicle_changed.emit(value)

    #input_gcws_rail_design_warning_time_gate_arm_clearance
    @property
    def input_gcws_rail_design_warning_time_gate_arm_clearance(self):
        return self.input_gcws_rail_design_warning_time_gate_arm_clearance

    @input_gcws_rail_design_warning_time_gate_arm_clearance.setter
    def input_gcws_rail_design_warning_time_gate_arm_clearance(self, value):
        self._input_gcws_rail_design_warning_time_gate_arm_clearance = value
        self.input_gcws_rail_design_warning_time_gate_arm_clearance_changed.emit(value)

    #input_gcws_rail_design_warning_time_preemption
    @property
    def input_gcws_rail_design_warning_time_preemption(self):
        return self.input_gcws_rail_design_warning_time_preemption

    @input_gcws_rail_design_warning_time_preemption.setter
    def input_gcws_rail_design_warning_time_preemption(self, value):
        self._input_gcws_rail_design_warning_time_preemption = value
        self.input_gcws_rail_design_warning_time_preemption_changed.emit(value)

    #input_gcws_rail_design_warning_time_ssd
    @property
    def input_gcws_rail_design_warning_time_ssd(self):
        return self.input_gcws_rail_design_warning_time_ssd

    @input_gcws_rail_design_warning_time_ssd.setter
    def input_gcws_rail_design_warning_time_ssd(self, value):
        self._input_gcws_rail_design_warning_time_ssd = value
        self.input_gcws_rail_design_warning_time_ssd_changed.emit(value)

    # FLASHING LIGHT UNITS (GCS SECTION 13 & 14)
    #Group TextEdits
    #input_light_units_comments = None

    #Group LineEdits
    #input_light_units_measure_cantilevers_n_or_e_approach_distance_from_rail = None 
    #input_light_units_measure_cantilevers_n_or_e_approach_distance_from_road = None 
    #input_light_units_measure_cantilevers_n_or_e_approach_dl = None 
    #input_light_units_measure_cantilevers_n_or_e_approach_dr = None 
    #input_light_units_measure_cantilevers_n_or_e_approach_height = None 
    #input_light_units_measure_cantilevers_s_or_w_approach_distance_from_rail = None 
    #input_light_units_measure_cantilevers_s_or_w_approach_distance_from_road = None 
    #input_light_units_measure_cantilevers_s_or_w_approach_dl = None 
    #input_light_units_measure_cantilevers_s_or_w_approach_dr = None 
    #input_light_units_measure_cantilevers_s_or_w_approach_height = None 
    #input_light_units_measure_n_or_e_approach_height = None 
    #input_light_units_measure_s_or_w_approach_height = None 

    #Group ComboBoxes
    #input_light_units_observe_cantilevers_per_fig_12_3 = None
    #input_light_units_observe_per_fig_12_1 = None
    #input_light_units_observe_sidewalks_n_or_e_approach = None
    #input_light_units_observe_sidewalks_s_or_w_approach = None
    #input_light_units_observe_supplemental_lights_n_or_e_approach = None
    #input_light_units_observe_supplemental_lights_s_or_w_approach = None
    #input_light_units_observe_visibility_back_lights_n_or_e_approach = None
    #input_light_units_observe_visibility_back_lights_s_or_w_approach = None
    #input_light_units_observe_visibility_front_lights_n_or_e_approach = None
    #input_light_units_observe_visibility_front_lights_s_or_w_approach = None

    # GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)
    #Group TextEdits
    #input_gates_gcws_comments = None

    #Group LineEdits
    #input_gates_gcws_measure_distance_between_gate_end_and_road_cl_n_or_e_approach = None 
    #input_gates_gcws_measure_distance_between_gate_end_and_road_cl_s_or_w_approach = None 
    #input_gates_gcws_measure_gate_ascent_time = None 
    #input_gates_gcws_measure_gate_descent_time = None 
    #input_gates_gcws_rail_gate_arm_delay_time_design = None 

    #input_gates_gcws_rail_gate_arm_descent_time_design
    @property
    def input_gates_gcws_rail_gate_arm_descent_time_design(self):
        return self.input_gates_gcws_rail_gate_arm_descent_time_design

    @input_gates_gcws_rail_gate_arm_descent_time_design.setter
    def input_gates_gcws_rail_gate_arm_descent_time_design(self, value):
        self._input_gates_gcws_rail_gate_arm_descent_time_design = value
        self.input_gates_gcws_rail_gate_arm_descent_time_design_changed.emit(value)

    #input_gates_gcws_rail_inner_gate_arm_delay_time_design = None 

    #Group Labels
    #input_gates_gcws_calculate_gate_arm_clearance_time_recommended
    @property
    def input_gates_gcws_calculate_gate_arm_clearance_time_recommended(self):
        return self.input_gates_gcws_calculate_gate_arm_clearance_time_recommended

    @input_gates_gcws_calculate_gate_arm_clearance_time_recommended.setter
    def input_gates_gcws_calculate_gate_arm_clearance_time_recommended(self, value):
        self._input_gates_gcws_calculate_gate_arm_clearance_time_recommended = value
        self.input_gates_gcws_calculate_gate_arm_clearance_time_recommended_changed.emit(value)

    #input_gates_gcws_calculate_inner_gate_arm_delay_time_recommended
    @property
    def input_gates_gcws_calculate_inner_gate_arm_delay_time_recommended(self):
        return self.input_gates_gcws_calculate_inner_gate_arm_delay_time_recommended

    @input_gates_gcws_calculate_inner_gate_arm_delay_time_recommended.setter
    def input_gates_gcws_calculate_inner_gate_arm_delay_time_recommended(self, value):
        self._input_gates_gcws_calculate_inner_gate_arm_delay_time_recommended = value
        self.input_gates_gcws_calculate_inner_gate_arm_delay_time_recommended_changed.emit(value)

    #Group ComboBoxes
    #input_gates_gcws_observe_gate_arm_rest = None
    #input_gates_gcws_observe_gate_ascent_time = None
    #input_gates_gcws_observe_gate_descent_time = None
    #input_gates_gcws_observe_gate_strips_n_or_e_approach = None
    #input_gates_gcws_observe_gate_strips_s_or_w_approach = None
    #input_gates_gcws_observe_per_fig_12_2 = None

    # PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)
    #Group Text Edits
    #input_aawd_comments = None

    #Group LineEdits
    #input_aawd_measure_distance_sign_and_stop_n_or_e_approach_actual = None 
    #input_aawd_measure_distance_sign_and_stop_s_or_w_approach_actual = None 

    #Group ComboBoxes
    #input_aawd_observe_present_n_or_e_approach = None
    #input_aawd_observe_present_s_or_w_approach = None
    #input_aawd_road_aawd_sufficient_activation_time_n_or_e_approach = None
    #input_aawd_road_aawd_sufficient_activation_time_s_or_w_approach = None

    #Group Labels
    #input_aawd_calculate_advance_activation_time_design_n_or_e_approach
    @property
    def input_aawd_calculate_advance_activation_time_design_n_or_e_approach(self):
        return self.input_aawd_calculate_advance_activation_time_design_n_or_e_approach

    @input_aawd_calculate_advance_activation_time_design_n_or_e_approach.setter
    def input_aawd_calculate_advance_activation_time_design_n_or_e_approach(self, value):
        self._input_aawd_calculate_advance_activation_time_design_n_or_e_approach = value
        self.input_aawd_calculate_advance_activation_time_design_n_or_e_approach_changed.emit(value)

    #input_aawd_calculate_advance_activation_time_design_s_or_w_approach
    @property
    def input_aawd_calculate_advance_activation_time_design_s_or_w_approach(self):
        return self.input_aawd_calculate_advance_activation_time_design_s_or_w_approach

    @input_aawd_calculate_advance_activation_time_design_s_or_w_approach.setter
    def input_aawd_calculate_advance_activation_time_design_s_or_w_approach(self, value):
        self._input_aawd_calculate_advance_activation_time_design_s_or_w_approach = value
        self.input_aawd_calculate_advance_activation_time_design_s_or_w_approach_changed.emit(value)

    #input_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended
    @property
    def input_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended(self):
        return self.input_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended

    @input_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended.setter
    def input_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended(self, value):
        self._input_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended = value
        self.input_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended_changed.emit(value)

    #input_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended
    @property
    def input_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended(self):
        return self.input_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended

    @input_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended.setter
    def input_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended(self, value):
        self._input_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended = value
        self.input_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended_changed.emit(value)

    #input_aawd_warrant_gcr_lookup_road_classification
    @property
    def input_aawd_warrant_gcr_lookup_road_classification(self):
        return self.input_aawd_warrant_gcr_lookup_road_classification

    @input_aawd_warrant_gcr_lookup_road_classification.setter
    def input_aawd_warrant_gcr_lookup_road_classification(self, value):
        self._input_aawd_warrant_gcr_lookup_road_classification = value
        self.input_aawd_warrant_gcr_lookup_road_classification_changed.emit(value)

    #input_aawd_warrant_gcr_observe_environmental_condition
    @property
    def input_aawd_warrant_gcr_observe_environmental_condition(self):
        return self.input_aawd_warrant_gcr_observe_environmental_condition

    @input_aawd_warrant_gcr_observe_environmental_condition.setter
    def input_aawd_warrant_gcr_observe_environmental_condition(self, value):
        self._input_aawd_warrant_gcr_observe_environmental_condition = value
        self.input_aawd_warrant_gcr_observe_environmental_condition_changed.emit(value)

    #input_aawd_warrant_gcr_observe_sightline_obstruction
    @property
    def input_aawd_warrant_gcr_observe_sightline_obstruction(self):
        return self.input_aawd_warrant_gcr_observe_sightline_obstruction

    @input_aawd_warrant_gcr_observe_sightline_obstruction.setter
    def input_aawd_warrant_gcr_observe_sightline_obstruction(self, value):
        self._input_aawd_warrant_gcr_observe_sightline_obstruction = value
        self.input_aawd_warrant_gcr_observe_sightline_obstruction_changed.emit(value)

    #input_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr
    @property
    def input_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr(self):
        return self.input_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr

    @input_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr.setter
    def input_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr(self, value):
        self._input_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr = value
        self.input_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr_changed.emit(value)

    #input_aawd_warrant_mutcd_lookup_significant_road_downgrade
    @property
    def input_aawd_warrant_mutcd_lookup_significant_road_downgrade(self):
        return self.input_aawd_warrant_mutcd_lookup_significant_road_downgrade

    @input_aawd_warrant_mutcd_lookup_significant_road_downgrade.setter
    def input_aawd_warrant_mutcd_lookup_significant_road_downgrade(self, value):
        self._input_aawd_warrant_mutcd_lookup_significant_road_downgrade = value
        self.input_aawd_warrant_mutcd_lookup_significant_road_downgrade_changed.emit(value)

    # INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)
    #Group TextEdits
    #input_preemption_of_traffic_signals_comments = None

    #Group LineEdits
    #input_preemption_of_traffic_signals_road_preemption_warning_time_actual = None 
    #input_preemption_of_traffic_signals_road_preemption_warning_time_design = None 

    #Group CombBoxes
    #input_preemption_of_traffic_signals_observe_consideration_of_Longer_vehicles = None
    #input_preemption_of_traffic_signals_observe_known_queuing_issues = None
    #input_preemption_of_traffic_signals_observe_pedestrian_accommodation = None
    #input_preemption_of_traffic_signals_observe_queuing_condition = None
    #input_preemption_of_traffic_signals_observe_supplemental_signage = None
    #input_preemption_of_traffic_signals_observe_traffic_clearance_time_adequate = None
    #input_preemption_of_traffic_signals_observe_unintended_queuing_by_traffic_signals = None
    #input_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type = None

    #Group DatePicker
    #input_preemption_of_traffic_signals_road_date_Last_preemption_check = None

    #Group Labels
    #input_preemption_of_traffic_signals_lookup_proximity_condition
    @property
    def input_preemption_of_traffic_signals_lookup_proximity_condition(self):
        return self.input_preemption_of_traffic_signals_lookup_proximity_condition

    @input_preemption_of_traffic_signals_lookup_proximity_condition.setter
    def input_preemption_of_traffic_signals_lookup_proximity_condition(self, value):
        self._input_preemption_of_traffic_signals_lookup_proximity_condition = value
        self.input_preemption_of_traffic_signals_lookup_proximity_condition_changed.emit(value)

    #input_preemption_of_traffic_signals_lookup_required
    @property
    def input_preemption_of_traffic_signals_lookup_required(self):
        return self.input_preemption_of_traffic_signals_lookup_required

    @input_preemption_of_traffic_signals_lookup_required.setter
    def input_preemption_of_traffic_signals_lookup_required(self, value):
        self._input_preemption_of_traffic_signals_lookup_required = value
        self.input_preemption_of_traffic_signals_lookup_required_changed.emit(value)

    # WHISTLE CESSATION (GCS SECTION Appendix D)
    #Group TextEdits
    #input_areas_without_train_whistling_comments = None

    #Group ComboBoxes
    #input_areas_without_train_whistling_observe_for_stop_and_proceed = None
    #input_areas_without_train_whistling_observe_tresNoneing_area = None
    #input_areas_without_train_whistling_rail_anti_whistling_zone = None
    #input_areas_without_train_whistling_rail_anti_whistling_zone_24_hrs = None

    #Group Labels
    #input_areas_without_train_whistling_lookup_gcs_12_to_16
    @property
    def input_areas_without_train_whistling_lookup_gcs_12_to_16(self):
        return self.input_areas_without_train_whistling_lookup_gcs_12_to_16

    @input_areas_without_train_whistling_lookup_gcs_12_to_16.setter
    def input_areas_without_train_whistling_lookup_gcs_12_to_16(self, value):
        self._input_areas_without_train_whistling_lookup_gcs_12_to_16 = value
        self.input_areas_without_train_whistling_lookup_gcs_12_to_16_changed.emit(value)

    #input_areas_without_train_whistling_lookup_gcs_9_2
    @property
    def input_areas_without_train_whistling_lookup_gcs_9_2(self):
        return self.input_areas_without_train_whistling_lookup_gcs_9_2

    @input_areas_without_train_whistling_lookup_gcs_9_2.setter
    def input_areas_without_train_whistling_lookup_gcs_9_2(self, value):
        self._input_areas_without_train_whistling_lookup_gcs_9_2 = value
        self.input_areas_without_train_whistling_lookup_gcs_9_2_changed.emit(value)

    #input_areas_without_train_whistling_requirements_observe_table_D1
    @property
    def input_areas_without_train_whistling_requirements_observe_table_D1(self):
        return self.input_areas_without_train_whistling_requirements_observe_table_D1

    @input_areas_without_train_whistling_requirements_observe_table_D1.setter
    def input_areas_without_train_whistling_requirements_observe_table_D1(self, value):
        self._input_areas_without_train_whistling_requirements_observe_table_D1 = value
        self.input_areas_without_train_whistling_requirements_observe_table_D1_changed.emit(value)

    def __init__(self):
        super().__init__()

        # INSPECTION DETAILS
        #Group TextBoxes
        #self._input_inspection_details_assessment_team = None
        
        #Group DatePicker
        #self._input_inspection_details_date_assessment = None
        
        #Group LineEdits
        #self._input_inspection_details_crossing_location = None 
        #self._input_inspection_details_latitude = None 
        #self._input_inspection_details_location_number = None 
        #self._input_inspection_details_longitude = None 
        #self._input_inspection_details_municipality = None 
        #self._input_inspection_details_road_name = None 
        #self._input_inspection_details_road_number = None 
        #self._input_inspection_details_spur_mile = None 
        #self._input_inspection_details_spur_name = None 
        #self._input_inspection_details_subdivision_mile = None 

        #Group ComboBoxes
        self._input_inspection_details_gcws_type = None
        self._input_inspection_details_grade_crossing_type = None
        #self._input_inspection_details_province = None
        #self._input_inspection_details_railway_authority = None
        #self._input_inspection_details_reason_for_assessment = None
        #self._input_inspection_details_road_authority = None
        #self._input_inspection_details_subdivision_name = None
        #self._input_inspection_details_track_type = None

        # COLLISION HISTORY (5 YEAR PERIOD)
        #Group TextEdits
        #self._input_collision_history_comments = None

        #Group LineEdits
        self._input_collision_history_fatal_injury = None 
        #self._input_collision_history_fatalities = None 
        #self._input_collision_history_personal_injuries = None 
        self._input_collision_history_personal_injury = None 
        self._input_collision_history_property_damage = None

        #Group Labels
        self._input_collision_history_total_5_year_period = 'No Value' 

        # GENERAL INFORMATION
        #Group TextEdits
        #self._input_general_info_comments = None

        #Group LineEdits
        #self._input_general_info_observe_special_buildings = None 
        self._input_general_info_rail_max_railway_operating_speed_freight = None 
        self._input_general_info_rail_max_railway_operating_speed_passenger = None 
        self._input_general_info_rail_no_trains_per_day_freight = None 
        self._input_general_info_rail_no_trains_per_day_passengers = None
        self._input_general_info_rail_no_tracks_main = None
        self._input_general_info_rail_no_tracks_other = None
        self._input_general_info_rail_railway_design_speed = None 
        self._input_general_info_road_aadt_current = None 
        self._input_general_info_road_aadt_forecast = None 
        #self._input_general_info_road_aadt_year_current = None 
        #self._input_general_info_road_aadt_year_forecasted = None 
        #self._input_general_info_road_cyclist_per_day = None 
        self._input_general_info_road_no_traffic_lanes_bidirectional = None 
        self._input_general_info_road_no_traffic_lanes_northbound_or_eastbound = None 
        self._input_general_info_road_no_traffic_lanes_southbound_or_westbound = None 
        #self._input_general_info_road_other_users = None 
        #self._input_general_info_road_other_users_daily_users = None 
        #self._input_general_info_road_pedestrians_per_day = None 
        self._input_general_info_road_speed_design = None 
        #self._input_general_info_road_speed_posted = None 

        #Group ComboBoxes
        #self._input_general_info_observe_roadway_illumination = None
        #self._input_general_info_observe_surrounding_land_use = None
        #self._input_general_info_rail_train_switching = None        
        #self._input_general_info_road_assistive_pedestrian_devices = None
        self._input_general_info_road_classification = None        
        #self._input_general_info_road_dangerous_goods_route = None
        #self._input_general_info_road_school_bus_route = None
        #self._input_general_info_road_seasonal_volume_fluctuations = None
        self._input_general_info_road_sidewalks = None

        #Group Labels
        self._input_general_info_rail_no_tracks_total = 'No Value'
        self._input_general_info_rail_no_trains_per_day_total = 'No Value'
        self._input_general_info_road_no_traffic_lanes_total = 'No Value'

        # DESIGN CONSIDERATIONS (GCS SECTION 10)
        #Group TextEdits
        #self._input_design_comments = None

        #Group LineEdits
        self._input_design_measure_adjacent_track_clearance_distance = None 
        self._input_design_measure_adjacent_track_separation_distance = None 
        self._input_design_measure_clearance_distance_pedestrian = None 
        self._input_design_measure_clearance_distance_vehicle = None 
        self._input_design_road_max_approach_grade_within_s = None 

        #Group ComboBoxes
        #self._input_design_observe_field_acceleration_times_exceed_td = None
        self._input_design_road_design_vehicle_type = None

        #Group Labels
        self._input_design_calculate_adjacent_track_clearance_time = 'No Value'
        self._input_design_calculate_clearance_time_crossing_pedestrian_design_check = 'No Value'
        self._input_design_calculate_clearance_time_crossing_vehicle_design_check = 'No Value'
        self._input_design_calculate_clearance_time_gate_arm_ssd = 'No Value'
        self._input_design_calculate_clearance_time_gate_arm_stop = 'No Value'
        self._input_design_calculate_vehicle_travel_distance = 'No Value'
        self._input_design_input_reaction_time = 'No Value'
        self._input_design_lookup_design_vehicle_class = 'No Value'
        self._input_design_lookup_design_vehicle_length = 'No Value'
        self._input_design_lookup_grade_adjustment_factor = 'No Value'
        self._input_design_lookup_vehicle_departure_time_crossing = 'No Value'
        self._input_design_lookup_vehicle_departure_time_gate_arm_clearance = 'No Value'
        
        # LOCATION OF GRADE CROSSING (GCS SECTION 11)
        #Group TextEdits
        #self._input_location_of_grade_crossing_comments = None

        #Group LineEdits
        #self._input_location_of_grade_crossing_nearest_intersection_other_n_or_e_approach = None 
        #self._input_location_of_grade_crossing_nearest_intersection_other_s_of_w_approach = None 
        self._input_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach = None 
        self._input_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach = None 
        self._input_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach = None 
        self._input_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach = None 

        #group ComboBoxes
        #self._input_location_of_grade_crossing_observe_nearby_pedestrian_crosswalk = None
        #self._input_location_of_grade_crossing_queue_condition = None
        #self._input_location_of_grade_crossing_visibility_of_warning_lights = None
        
        # GRADE CROSSING SURFACE (GCS SECTION 5)
        #Group TextEdits
        #self._input_grade_crossing_surface_comments = None

        #Group LineEdits
        #self._input_grade_crossing_surface_measure_crossing_surface_extension_n_or_e_approach = None 
        #self._input_grade_crossing_surface_measure_crossing_surface_extension_s_or_w_approach = None 
        #self._input_grade_crossing_surface_measure_crossing_surface_width = None 
        #self._input_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_n_or_e_approach = None 
        #self._input_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_s_or_w_approach = None 
        #self._input_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_n_or_e_approach = None 
        #self._input_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_s_or_w_approach = None 
        #self._input_grade_crossing_surface_measure_elevation_top_of_rail_above_road_surface = None 
        #self._input_grade_crossing_surface_measure_elevation_top_of_rail_below_road_surface = None 
        #self._input_grade_crossing_surface_measure_flangeway_depth = None 
        #self._input_grade_crossing_surface_measure_flangeway_width = None 
        #self._input_grade_crossing_surface_measure_road_surface_median_width = None 
        #self._input_grade_crossing_surface_measure_road_surface_shoulder_n_or_e_approach = None 
        #self._input_grade_crossing_surface_measure_road_surface_shoulder_s_or_w_approach = None 
        #self._input_grade_crossing_surface_measure_road_surface_travel_lanes_width_n_or_e_approach = None 
        #self._input_grade_crossing_surface_measure_road_surface_travel_lanes_width_s_or_w_approach = None 
        #self._input_grade_crossing_surface_measure_side_grinding_depth = None 
        #self._input_grade_crossing_surface_measure_side_grinding_width = None 
        #self._input_grade_crossing_surface_measure_sidewalk_extension_n_or_e_approach = None 
        #self._input_grade_crossing_surface_measure_sidewalk_extension_s_or_w_approach = None 
        #self._input_grade_crossing_surface_measure_sidewalk_width_n_or_e_approach = None 
        #self._input_grade_crossing_surface_measure_sidewalk_width_s_or_w_approach = None 

        #Group ComboBoxes
        #self._input_grade_crossing_surface_observe_crossing_smoothness = None
        #self._input_grade_crossing_surface_observe_crossing_surface_condition = None
        #self._input_grade_crossing_surface_observe_material = None
        #self._input_grade_crossing_surface_observe_road_approach_surface_condition = None
        #self._input_grade_crossing_surface_observe_road_approach_surface_type = None

        # ROAD GEOMETRY (GCS SECTION 6)
        #Group TextEdits 
        #self._input_road_geometry_comments = None

        #Group LineEdits
        self._input_road_geometry_measure_railway_cross_slope = None 
        #self._input_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_n_or_e_approach = None 
        #self._input_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_s_or_w_approach = None 
        #self._input_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_n_or_e_approach = None 
        #self._input_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_s_or_w_approach = None 
        self._input_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach = None 
        self._input_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach = None 
        self._input_road_geometry_rail_superelevation_n_or_e_approach = None 
        self._input_road_geometry_rail_superelevation_s_or_w_approach = None 
        #self._input_road_geometry_road_crossing_angle = None 
        self._input_road_geometry_road_general_approach_grade_n_or_e_approach = None 
        self._input_road_geometry_road_general_approach_grade_s_or_w_approach = None 

        #Group ComboBoxes
        #self._input_road_geometry_observe_lane_width_crossing_vs_approach_n_or_e_approach = None
        #self._input_road_geometry_observe_lane_width_crossing_vs_approach_s_or_w_approach = None
        #self._input_road_geometry_observe_low_bed_truck_condition = None
        #self._input_road_geometry_observe_smooth_alignment_within_ssd_n_or_e_approach = None
        #self._input_road_geometry_observe_smooth_alignment_within_ssd_s_or_w_approach = None
       
        #Group Labels
        self._input_road_geometry_lookup_gradient_difference = 'No Value'
        
        # SIGHTLINES (GCS SECTION 7)
        #Group TextEdits
        #self._input_sightlines_comments = None
        
        #Group LineEdits
        #self._input_sightlines_measure_dssd_actual_n_or_e_approach_left = None 
        #self._input_sightlines_measure_dssd_actual_n_or_e_approach_right = None 
        #self._input_sightlines_measure_dssd_actual_s_or_w_approach_left = None 
        #self._input_sightlines_measure_dssd_actual_s_or_w_approach_right = None 
        #self._input_sightlines_measure_dstopped_actual_n_or_e_approach_driver_left = None 
        #self._input_sightlines_measure_dstopped_actual_n_or_e_approach_driver_right = None 
        #self._input_sightlines_measure_dstopped_actual_s_or_w_approach_driver_left = None 
        #self._input_sightlines_measure_dstopped_actual_s_or_w_approach_driver_right = None 
        #self._input_sightlines_measure_ssd_actual_n_or_e_approach = None 
        #self._input_sightlines_measure_ssd_actual_s_or_w_approach = None 

        #Group ComboBoxes
        #self._input_sightlines_observe_sightline_obstructions = None

        #Group Labels
        self._input_sightlines_calculate_dssd_vehicle_min_ft = 'No Value'
        self._input_sightlines_calculate_dssd_vehicle_min_m = 'No Value'
        self._input_sightlines_calculate_dstopped_pedestrian_min_ft = 'No Value'
        self._input_sightlines_calculate_dstopped_pedestrian_min_m = 'No Value'
        self._input_sightlines_calculate_dstopped_vehicle_min_ft = 'No Value'
        self._input_sightlines_calculate_dstopped_vehicle_min_m = 'No Value'
        self._input_sightlines_lookup_ssd_minimum_n_or_e_approach = 'No Value'
        self._input_sightlines_lookup_ssd_minimum_s_or_w_approach = 'No Value'

        # SIGNS AND PAVEMENT MARKINGS (GCS SECTION 8)
        #Group TextEdits
        #DELETE self._input_signs_and_markings_advisory_speed_comments = None
        #DELETE self._input_signs_and_markings_comments = None
        #DELETE self._input_signs_and_markings_emergency_notification_comments = None
        #DELETE self._input_signs_and_markings_number_of_tracks_comments = None
        #DELETE self._input_signs_and_markings_railway_crossing_ahead_comments = None
        #DELETE self._input_signs_and_markings_railway_crossing_comments = None
        #DELETE self._input_signs_and_markings_stop_comments = None
        #DELETE self._input_signs_and_markings_stop_sign_ahead_comments = None

        #Group LineEdits
        #self._input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_rail = None 
        #self._input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_road = None 
        #self._input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_height = None 
        #self._input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_rail = None 
        #self._input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_road = None 
        #self._input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_height = None 
        #self._input_signs_and_markings_stop_n_or_e_approach_height = None 
        #self._input_signs_and_markings_stop_n_or_e_approach_location_from_rail = None 
        #self._input_signs_and_markings_stop_n_or_e_approach_location_from_road = None 
        #self._input_signs_and_markings_stop_s_or_w_approach_height = None 
        #self._input_signs_and_markings_stop_s_or_w_approach_location_from_rail = None 
        #self._input_signs_and_markings_stop_s_or_w_approach_location_from_road = None 
        #self._input_signs_and_markings_stop_sign_ahead_n_or_e_approach_height = None 
        #self._input_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_rail = None 
        #self._input_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_road = None 
        #self._input_signs_and_markings_stop_sign_ahead_s_or_w_approach_height = None 
        #self._input_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_rail = None 
        #self._input_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_road = None 

        #Group ComboBoxes
        #self._input_signs_and_markings_advisory_speed_n_or_e_approach_present = None
        #self._input_signs_and_markings_advisory_speed_n_or_e_approach_with_wa_18_20 = None
        #self._input_signs_and_markings_advisory_speed_s_or_w_approach_present = None
        #self._input_signs_and_markings_advisory_speed_s_or_w_approach_with_wa_18_20 = None
        #self._input_signs_and_markings_dividing_lines_present = None
        #self._input_signs_and_markings_emergency_notification_n_or_e_approach_condition = None
        #self._input_signs_and_markings_emergency_notification_n_or_e_approach_legible = None
        #self._input_signs_and_markings_emergency_Notification_n_or_e_approach_orientation = None
        #self._input_signs_and_markings_emergency_notification_n_or_e_approach_present = None
        #self._input_signs_and_markings_emergency_notification_s_or_w_approach_condition = None
        #self._input_signs_and_markings_emergency_notification_s_or_w_approach_legible = None
        #self._input_signs_and_markings_emergency_notification_s_or_w_approach_orientation = None
        #self._input_signs_and_markings_emergency_notification_s_or_w_approach_present = None
        #self._input_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_1b = None
        #self._input_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_3c = None
        #self._input_signs_and_markings_number_of_tracks_n_or_e_approach_present = None
        #self._input_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_1b = None
        #self._input_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_3c = None
        #self._input_signs_and_markings_number_of_tracks_s_or_w_approach_present = None
        #self._input_signs_and_markings_per_mutcd = None
        #self._input_signs_and_markings_posted_speed_n_or_e_approach_present = None
        #self._input_signs_and_markings_posted_speed_s_or_w_approach_present = None
        #self._input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_orientation = None
        #self._input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_present = None
        #self._input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_orientation = None
        #self._input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_present = None
        #self._input_signs_and_markings_railway_crossing_n_or_e_approach_per_fig_8_1a = None
        #self._input_signs_and_markings_railway_crossing_n_or_e_approach_present = None
        #self._input_signs_and_markings_railway_crossing_s_or_w_approach_per_fig_8_1a = None
        #self._input_signs_and_markings_railway_crossing_s_or_w_approach_present = None
        #self._input_signs_and_markings_sidewalks_present = None
        #self._input_signs_and_markings_stop_n_or_e_approach_per_fig_8_4 = None
        #self._input_signs_and_markings_stop_n_or_e_approach_present = None
        #self._input_signs_and_markings_stop_n_or_e_approach_same_post = None
        #self._input_signs_and_markings_stop_s_or_w_approach_per_fig_8_4 = None
        #self._input_signs_and_markings_stop_s_or_w_approach_present = None
        #self._input_signs_and_markings_stop_s_or_w_approach_same_post = None
        #self._input_signs_and_markings_stop_sign_ahead_n_or_e_approach_present = None
        #self._input_signs_and_markings_stop_sign_ahead_s_or_w_approach_present = None

        # GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)
        # Group Labels
        self._input_gcws_warrant_private_9_3 = 'No Value'
        self._input_gcws_warrant_private_9_3_1 = 'No Value'
        self._input_gcws_warrant_private_9_3_2_a = 'No Value'
        self._input_gcws_warrant_private_9_3_2_b = 'No Value'
        self._input_gcws_warrant_private_9_3_2_c = 'No Value'
        self._input_gcws_warrant_public_9_1 = 'No Value'
        self._input_gcws_warrant_public_9_1_a = 'No Value'
        self._input_gcws_warrant_public_9_1_b = 'No Value'
        self._input_gcws_warrant_public_9_1_c = 'No Value'
        self._input_gcws_warrant_public_9_1_d_i = 'No Value'
        self._input_gcws_warrant_public_9_1_d_ii = 'No Value'
        self._input_gcws_warrant_public_9_1_d_iii = 'No Value'
        self._input_gcws_warrant_sidewalk_9_5 = 'No Value'
        self._input_gates_gcws_warrant_private_9_4_1_a = 'No Value'
        self._input_gates_gcws_warrant_private_9_4_1_b = 'No Value'
        self._input_gates_gcws_warrant_private_9_4_1_c = 'No Value'
        self._input_gates_gcws_warrant_public_9_2_1_a = 'No Value'
        self._input_gates_gcws_warrant_public_9_2_1_b = 'No Value'
        self._input_gates_gcws_warrant_public_9_2_1_c = 'No Value'
        self._input_gates_gcws_warrant_public_9_2_1_d = 'No Value'
        self._input_gates_gcws_warrant_public_9_2_1_e = 'No Value'
        self._input_gates_gcws_warrant_sidewalk_9_6 = 'No Value'
        #self._input_gcws_warrants_comments = None

        # GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)
        #Group TextEdits
        #self._input_gcws_comments = None
         
        #Group LineEdits
        #self._input_gcws_measure_warning_device_n_or_e_approach_distance_from_rail = None 
        #self._input_gcws_measure_warning_device_n_or_e_approach_distance_from_road = None 
        #self._input_gcws_measure_warning_device_n_or_e_approach_distance_top_of_foundation = None 
        #self._input_gcws_measure_warning_device_n_or_e_approach_slope_from_foundation = None 
        #self._input_gcws_measure_warning_device_s_or_w_approach_distance_from_rail = None 
        #self._input_gcws_measure_warning_device_s_or_w_approach_distance_from_road = None 
        #self._input_gcws_measure_warning_device_s_or_w_approach_distance_top_of_foundation = None 
        #self._input_gcws_measure_warning_device_s_or_w_approach_slope_from_foundation = None 
        #self._input_gcws_rail_crossing_warning_time_actual = None 

        #Group ComboBox
        #self._input_gcws_observe_bell_if_sidewalk = None
        #self._input_gcws_observe_bells_condition = None
        #self._input_gcws_observe_bells_n_or_e_approach = None
        #self._input_gcws_observe_bells_s_or_w_approach = None
        #self._input_gcws_observe_cantilever_lights_condition = None
        #self._input_gcws_observe_cantilever_lights_n_or_e_approach = None
        #self._input_gcws_observe_cantilever_lights_s_or_w_approach = None
        #self._input_gcws_observe_gates_condition = None
        #self._input_gcws_observe_gates_n_or_e_approach = None
        #self._input_gcws_observe_gates_s_or_w_approach = None
        #self._input_gcws_observe_gcws_limited_use_with_walk_light_assembly = None
        #self._input_gcws_observe_gcws_limited_use_without_walk_light_assembly = None
        #self._input_gcws_observe_light_units_condition = None
        #self._input_gcws_observe_light_units_n_or_e_approach = None
        #self._input_gcws_observe_light_units_s_or_w_approach = None
        #self._input_gcws_observe_warning_time_consistency = None   
        #self._input_gcws_observe_warning_time_consistency_reduced_speed = None
        #self._input_gcws_rail_cut_out_circuit_requirements = None
        #self._input_gcws_rail_directional_stick_circuit_requirements = None
        #self._input_gcws_rail_self_diagnostic = None

        #Group Labels
        self._input_gcws_rail_design_approach_warning_time = 'No Value'
        self._input_gcws_rail_design_warning_time_adjacent_crossing = 'No Value'
        self._input_gcws_rail_design_warning_time_clearance_distance = 'No Value'
        self._input_gcws_rail_design_warning_time_departure_time_pedestrian = 'No Value'
        self._input_gcws_rail_design_warning_time_departure_time_vehicle = 'No Value'
        self._input_gcws_rail_design_warning_time_gate_arm_clearance = 'No Value'
        self._input_gcws_rail_design_warning_time_preemption = 'No Value'
        self._input_gcws_rail_design_warning_time_ssd = 'No Value'

        # FLASHING LIGHT UNITS (GCS SECTION 13 & 14)
        #Group TextEdits
        #self._input_light_units_comments = None

        #Group LineEdits
        #self._input_light_units_measure_cantilevers_n_or_e_approach_distance_from_rail = None 
        #self._input_light_units_measure_cantilevers_n_or_e_approach_distance_from_road = None 
        #self._input_light_units_measure_cantilevers_n_or_e_approach_dl = None 
        #self._input_light_units_measure_cantilevers_n_or_e_approach_dr = None 
        #self._input_light_units_measure_cantilevers_n_or_e_approach_height = None 
        #self._input_light_units_measure_cantilevers_s_or_w_approach_distance_from_rail = None 
        #self._input_light_units_measure_cantilevers_s_or_w_approach_distance_from_road = None 
        #self._input_light_units_measure_cantilevers_s_or_w_approach_dl = None 
        #self._input_light_units_measure_cantilevers_s_or_w_approach_dr = None 
        #self._input_light_units_measure_cantilevers_s_or_w_approach_height = None 
        #self._input_light_units_measure_n_or_e_approach_height = None 
        #self._input_light_units_measure_s_or_w_approach_height = None 

        #Group ComboBoxes
        #self._input_light_units_observe_cantilevers_per_fig_12_3 = None
        #self._input_light_units_observe_per_fig_12_1 = None
        #self._input_light_units_observe_sidewalks_n_or_e_approach = None
        #self._input_light_units_observe_sidewalks_s_or_w_approach = None
        #self._input_light_units_observe_supplemental_lights_n_or_e_approach = None
        #self._input_light_units_observe_supplemental_lights_s_or_w_approach = None
        #self._input_light_units_observe_visibility_back_lights_n_or_e_approach = None
        #self._input_light_units_observe_visibility_back_lights_s_or_w_approach = None
        #self._input_light_units_observe_visibility_front_lights_n_or_e_approach = None
        #self._input_light_units_observe_visibility_front_lights_s_or_w_approach = None

        # GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)
        #Group TextEdits
        #self._input_gates_gcws_comments = None

        #Group LineEdits
        #self._input_gates_gcws_measure_distance_between_gate_end_and_road_cl_n_or_e_approach = None 
        #self._input_gates_gcws_measure_distance_between_gate_end_and_road_cl_s_or_w_approach = None 
        #self._input_gates_gcws_measure_gate_ascent_time = None 
        #self._input_gates_gcws_measure_gate_descent_time = None 
        #self._input_gates_gcws_rail_gate_arm_delay_time_design = None 
        self._input_gates_gcws_rail_gate_arm_descent_time_design = None 
        #self._input_gates_gcws_rail_inner_gate_arm_delay_time_design = None 

        #Group Labels
        self._input_gates_gcws_calculate_gate_arm_clearance_time_recommended = 'No Value'
        self._input_gates_gcws_calculate_inner_gate_arm_delay_time_recommended = 'No Value'

        #Group ComboBoxes
        #self._input_gates_gcws_observe_gate_arm_rest = None
        #self._input_gates_gcws_observe_gate_ascent_time = None
        #self._input_gates_gcws_observe_gate_descent_time = None
        #self._input_gates_gcws_observe_gate_strips_n_or_e_approach = None
        #self._input_gates_gcws_observe_gate_strips_s_or_w_approach = None
        #self._input_gates_gcws_observe_per_fig_12_2 = None

        # PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)
        #Group Text Edits
        #self._input_aawd_comments = None

        #Group LineEdits
        #self._input_aawd_measure_distance_sign_and_stop_n_or_e_approach_actual = None 
        #self._input_aawd_measure_distance_sign_and_stop_s_or_w_approach_actual = None 

        #Group ComboBoxes
        #self._input_aawd_observe_present_n_or_e_approach = None
        #self._input_aawd_observe_present_s_or_w_approach = None
        #self._input_aawd_road_aawd_sufficient_activation_time_n_or_e_approach = None
        #self._input_aawd_road_aawd_sufficient_activation_time_s_or_w_approach = None

        #Group Labels
        self._input_aawd_calculate_advance_activation_time_design_n_or_e_approach = 'No Value'
        self._input_aawd_calculate_advance_activation_time_design_s_or_w_approach = 'No Value'
        self._input_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended = 'No Value'
        self._input_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended = 'No Value'
        self._input_aawd_warrant_gcr_lookup_road_classification = 'No Value'
        self._input_aawd_warrant_gcr_observe_environmental_condition = 'No Value'
        self._input_aawd_warrant_gcr_observe_sightline_obstruction = 'No Value'
        self._input_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr = 'No Value'
        self._input_aawd_warrant_mutcd_lookup_significant_road_downgrade = 'No Value'

        # INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)
        #Group TextEdits
        #self._input_preemption_of_traffic_signals_comments = None
    
        #Group LineEdits
        #self._input_preemption_of_traffic_signals_road_preemption_warning_time_actual = None 
        #self._input_preemption_of_traffic_signals_road_preemption_warning_time_design = None 

        #Group CombBoxes
        #self._input_preemption_of_traffic_signals_observe_consideration_of_Longer_vehicles = None
        #self._input_preemption_of_traffic_signals_observe_known_queuing_issues = None
        #self._input_preemption_of_traffic_signals_observe_pedestrian_accommodation = None
        #self._input_preemption_of_traffic_signals_observe_queuing_condition = None
        #self._input_preemption_of_traffic_signals_observe_supplemental_signage = None
        #self._input_preemption_of_traffic_signals_observe_traffic_clearance_time_adequate = None
        #self._input_preemption_of_traffic_signals_observe_unintended_queuing_by_traffic_signals = None
        #self._input_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type = None

        #Group DatePicker
        #self._input_preemption_of_traffic_signals_road_date_Last_preemption_check = None

        #Group Labels
        self._input_preemption_of_traffic_signals_lookup_proximity_condition = 'No Value'
        self._input_preemption_of_traffic_signals_lookup_required = 'No Value'

        # WHISTLE CESSATION (GCS SECTION Appendix D)
        #Group TextEdits
        #self._input_areas_without_train_whistling_comments = None

        #Group ComboBoxes
        #self._input_areas_without_train_whistling_observe_for_stop_and_proceed = None
        #self._input_areas_without_train_whistling_observe_tresNoneing_area = None
        #self._input_areas_without_train_whistling_rail_anti_whistling_zone = None
        #self._input_areas_without_train_whistling_rail_anti_whistling_zone_24_hrs = None

        #Group Labels
        self._input_areas_without_train_whistling_lookup_gcs_12_to_16 = 'No Value'
        self._input_areas_without_train_whistling_lookup_gcs_9_2 = 'No Value'
        self._input_areas_without_train_whistling_requirements_observe_table_D1 = 'No Value'