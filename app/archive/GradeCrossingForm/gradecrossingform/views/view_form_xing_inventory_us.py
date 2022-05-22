import sys
import datetime
import math
from numpy import mat, result_type
from numpy.lib.histograms import _hist_bin_auto
import pandas as pd
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class ViewFormUSDOTCrossingInventory(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

        
    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle('US DOT Crossing Inventory Form')
        self.formWidgets()
        self.show()
   
    def formWidgets(self):
        """
        Create widgets that will be used in the application form. 
        """

        # Combo Box Lists
        list_yes_no = ['', 'Yes', 'No']
        list_yes_no_na = ['', 'Yes', 'No', 'N/A']
        list_yes_no_unknown = ['', 'Yes', 'No', 'Unknonwn']
        list_condition = ['', 'Good', 'Fair', 'Poor']
        list_general_initiating_agency = ['', 'Railroad', 'State']
        list_general_reason_for_update = ['', 'Changes in Existing Data', 'New Crossing', 'Closed Crossing or Abandoned']
        list_location_and_classification_info_xing_owner = ['', 'In', 'Near']
        list_location_and_classification_info_quiet_zone = ['', 'No', '24 hr', 'Partial', 'Unknown']
        list_location_and_classification_info_xing_type = ['', 'Public', 'Private', 'Pedestrian']
        list_location_and_classification_info_xing_position = ['', 'At Grade', 'RR Under', 'RR Over']
        list_location_and_classification_info_passenger_type = ['', 'AMTRAK', 'AMTRAK & Other', 'Other', 'None']
        list_location_and_classification_info_xing_private_category = ['', 'Farm', 'Residential', 'Recreational', 'Industrial', 'Commercial']

        list_inspection_details_gcws_type = ['','Active','Passive']
        list_inspection_details_grade_crossing_type = ['','Public', 'Private (CTA 102-Type)', 'Private (CTA 103-Type)']
        list_inspection_details_track_type = ['','Mainline', 'Industrial Spur', 'Mainline Spur', 'Yard, Other']
        list_inspection_details_province = ['', 'AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'ON', 'QC', 'SK', 'YT']
        list_inspection_details_reason_for_assessment = [
            "",
            "Periodic Assessment",
            "A Significant Change in Infrastructure",
            "Whistle Cessation",
            "2+ Fatal Collisions in 5-Year Period",
            "Other Collision Experience (see below)",
            "Receipt of a notice from a Railway Company, under Section 3 of the Notice of Railway Works Regulations. Ref. (GCR 12.(2))",
            "A change in the design vehicle and the sightlines at the grade crossing, which must meet the requirements in Section 20 of the GCR. Ref. (GCR 13 GCR 28.(c))",
            "An increase in the design speed of the road crossing, which will result in a change to the road approach's classification as set out in column B of the Table 10-2 of the Grade Crossings Standards (GCS). Ref. (GCR 13 GCR 28.(d))",
            "The location, gradient or crossing angle of a grade crossing has changed, and Articles 6 and 11 of the GCS must be applied in a manner that improves the overall safety of the grade crossing. Ref. (GCR 13 GCR 88.(1))",
            "An increase of the absolute gradient of a road approach to an existing grade crossing which meets the standards set out in Article 6.3 of the GCS. Ref. (GCR 13 GCR 88.(2))",
            "The number or width of traffic lanes of a road approach increases, or a shoulder is added or a shoulder's width is increased. The grade crossing must meet the standards set out in Articles 5.1 and 6.4 of the GCS. Ref. (GCR 13 GCR 89)",
            "A traffic signal is installed at a grade crossing that corresponds to the specifications set out in Article 19.1 of the GCS, the warning system must be interconnected with the traffic signal, and the interconnection must meet the standards set out in Articles 19.2 to 19.4 of the GCS. Ref. (GCR 13 GCR 90)",
            "A change in the design vehicle, which has resulted in a change to the period of time that the warning system must operate, before railway equipment reaches the crossing surface and therefore must meet the standards set out in Article 16.1 of the GCS. Ref. (GCR 13 GCR 91)",
            "Receipt of a notice from a Road Authority under Section 3 of the Notice of Railway Works Regulations. Ref. (GCR 4.(2))",
            "A line of railway is added within the sightlines of the grade crossing and the sightlines must meet the requirements in Section 20 of the GCR. Ref. (GCR 5 – GCR 28.(a))"
            "There is a change in the class of track referred to in column 1 of the table in article 7.1.2 of the Grade Crossing Standards (GCS),  taking into account the maximum allowable operating speeds set out in column 2 or 3 of that table. Sightlines at the grade crossing must meet the requirements in Section 20 of the GCR. Ref. (GCR 5 – GCR 28.(b))",
            "A new warning system is installed at a grade crossing and must meet the applicable standards set out in Articles 12 to 16 of the GCS. Ref. (GCR 5 – GCR 87.(1))",
            "A component of a warning system is modified or installed and must meet the applicable standards set out in Articles 12 and 16 of the GCS. Ref. (GCR 5 – GCR 87.(2))",
            "A new installation of a warning system, or the modification or installation of a component of a warning system which results from an increase in the railway design speed. The warning system or component must meet the applicable standards set out in Articles 12 and 16 of the GCS before the increase in the railway design speed takes effect. Ref. (GCR 5 – GCR 87.(3))"
            ]
        list_general_info_road_classification = ['', 'Rural Local Undivided', 'Rural Collector Undivided',
            'Rural Collector Divided', 'Rural Arterial Undivided', 'Rural Arterial Divided', 'Rural Freeway Divided',
            'Urban Local Undivided', 'Urban Collector Undivided', 'Urban Collector Divided', 'Urban Arterial Undivided',
            'Urban Arterial Divided', 'Private Road', 'Pedestrian Crossing']
        list_general_info_observe_surrounding_land_use = ['', 'Farm', 'Residential', 'Recreational', 'Industrial', 'Commercial']
        list_design_road_design_vehicle_type = ['', 'Passenger Cars, Vans, and Pickups', 'Light Single-Unit Trucks',
            'Medium Single-Unit Trucks', 'Heavy Single-Unit Trucks', 'WB-19 Tractor-Semitrailers', 
            'WB-20 Tractor-Semitrailers', 'A-Train Doubles (ATD)', 'B-Train Doubles', 'Standard Single-Unit Buses (B-12)',
            'Articulated Buses (A-Bus)', 'Intercity Buses (I-Bus)', 'Pedestrian Only']
        list_grade_crossing_surface_observe_material = ['', 'Timber', 'Asphalt', 'Asphalt and Flange', 
            'Concrete', 'Concrete and Rubber', 'Rubber', 'Metal', 'Unconsolidated', 'Other']
        list_grade_crossing_surface_observe_road_approach_surface_type = ['', 'Asphalt', 'Concrete', 'Gravel']
        list_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type = ['', 'Not Interconnected', 'Advance Preemption', 'Simultaneous Preemption']
                
        # General
        #Group TextBoxes
        '''
        #Group DatePicker
        self.datetimeEdit_general_effective_date = qtw.QDatetimeEdit(
            self,
            date=datetime.date.today(),
            calendarPopup=True,
            displayFormat='yyyy-MM-dd'
        )
        '''

        #Group LineEdits
        self.lineEdit_general_crossing_number = qtw.QLineEdit()  

        #Group ComboBoxes
        self.comboBox_general_initiating_agency = qtw.QComboBox()
        self.comboBox_general_initiating_agency.addItems(list_general_initiating_agency)

        self.comboBox_general_reason_for_update = qtw.QComboBox()
        self.comboBox_general_reason_for_update.addItems(list_general_reason_for_update)

        # Part I: Location and Classification Information
        #Group TextEdits
        self.textEdit_collision_history_comments = qtw.QTextEdit()

        #Group SpinBox
        self.spinBox_collision_history_fatal_injury = qtw.QSpinBox()
        self.spinBox_collision_history_fatal_injury.setRange(0, 999999)
        
        #Group Labels 
        self.label_collision_history_total_5_year_period = qtw.QLabel('No Value')
        
        # GENERAL INFORMATION
        #Group TextEdits
        self.lineEdit_location_and_classification_info_narrative = qtw.QTextEdit()

        #Group LineEdits
        self.lineEdit_location_and_classification_info_rr_operator_co = qtw.QLineEdit()
        self.lineEdit_location_and_classification_info_state = qtw.QLineEdit()
        self.lineEdit_location_and_classification_info_county = qtw.QLineEdit()
        self.lineEdit_location_and_classification_info_rr_division_or_region = qtw.QLineEdit()
        self.lineEdit_location_and_classification_info_rrsubdivision_or_district = qtw.QLineEdit()
        self.lineEdit_location_and_classification_info_branch_or_line_name = qtw.QLineEdit()
        self.lineEdit_location_and_classification_info_rr_milepost = qtw.QLineEdit()
        self.lineEdit_location_and_classification_info_rr_id = qtw.QLineEdit()
        self.lineEdit_location_and_classification_info_rr_timetable_station = qtw.QLineEdit()
        self.lineEdit_location_and_classification_info_rr_parent = qtw.QLineEdit()
        self.lineEdit_location_and_classification_info_xing_owner = qtw.QLineEdit()
        self.lineEdit_location_and_classification_info_road_name = qtw.QLineEdit()
        self.lineEdit_location_and_classification_info_hwy_type = qtw.QLineEdit()
        self.lineEdit_location_and_classification_info_rr_use = qtw.QLineEdit()
        self.lineEdit_location_and_classification_info_state_use = qtw.QLineEdit()
        self.lineEdit_location_and_classification_info_contact_emergency = qtw.QLineEdit()
        self.lineEdit_location_and_classification_info_contact_rr = qtw.QLineEdit()
        self.lineEdit_location_and_classification_info_contact_state = qtw.QLineEdit() 

        #Group SpinBox
        self.spinBox_location_and_classification_info_train_count_passenger = qtw.QSpinBox()
        self.spinBox_location_and_classification_info_train_count_passenger.setRange(0, 999999)
 
        #Group ComboBoxes
        self.comboBox_location_and_classification_info_xing_owner = qtw.QComboBox()
        self.comboBox_location_and_classification_info_xing_owner.addItems(list_location_and_classification_info_xing_owner)

        self.comboBox_location_and_classification_info_ens_sign = qtw.QComboBox()
        self.comboBox_location_and_classification_info_ens_sign.addItems(list_yes_no)

        self.comboBox_location_and_classification_info_quiet_zone = qtw.QComboBox()
        self.comboBox_location_and_classification_info_quiet_zone.addItems(list_location_and_classification_info_quiet_zone)

        self.comboBox_location_and_classification_info_xing_type = qtw.QComboBox()
        self.comboBox_location_and_classification_info_xing_type.addItems(list_location_and_classification_info_xing_type)

        self.comboBox_location_and_classification_info_xing_position = qtw.QComboBox()
        self.comboBox_location_and_classification_info_xing_position.addItems(list_location_and_classification_info_xing_position)

        self.comboBox_location_and_classification_info_passenger_type = qtw.QComboBox()
        self.comboBox_location_and_classification_info_passenger_type.addItems(list_location_and_classification_info_passenger_type)

        self.comboBox_location_and_classification_info_adjacent_xing = qtw.QComboBox()
        self.comboBox_location_and_classification_info_adjacent_xing.addItems(list_yes_no)

        self.comboBox_location_and_classification_info_xing_private_category = qtw.QComboBox()
        self.comboBox_location_and_classification_info_xing_private_category.addItems(list_location_and_classification_info_xing_private_category)

        self.comboBox_location_and_classification_info_xing_private_access = qtw.QComboBox()
        self.comboBox_location_and_classification_info_xing_private_access.addItems(list_yes_no_unknown)

        # DESIGN CONSIDERATIONS (GCS SECTION 10)
        #Group TextEdits
        self.textEdit_design_observe_k_factor_other = qtw.QTextEdit()
        self.textEdit_design_comments = qtw.QTextEdit()

        #Group DoubleSpinBox
        self.doubleSpinBox_design_measure_adjacent_track_clearance_distance = qtw.QDoubleSpinBox()
        self.doubleSpinBox_design_measure_adjacent_track_clearance_distance.setRange(0, 999999)

        self.doubleSpinBox_design_measure_adjacent_track_separation_distance = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_design_measure_adjacent_track_separation_distance.setRange(0, 999999)

        self.doubleSpinBox_design_measure_clearance_distance_pedestrian = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_design_measure_clearance_distance_pedestrian.setRange(0, 999999)

        self.doubleSpinBox_design_measure_clearance_distance_pedestrian_gate_arm_stop = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_design_measure_clearance_distance_pedestrian.setRange(0, 999999)

        self.doubleSpinBox_design_measure_clearance_distance_vehicle = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_design_measure_clearance_distance_vehicle.setRange(0, 50)

        self.doubleSpinBox_design_road_max_approach_grade_within_s = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_design_road_max_approach_grade_within_s.setRange(-999999, 999999)        

        #Group ComboBoxes
        self.comboBox_design_observe_k_factor_road_surface_condition = qtw.QComboBox()
        self.comboBox_design_observe_k_factor_road_surface_condition.addItems(list_yes_no)
		
        self.comboBox_design_observe_k_factor_crossing_surface_condition = qtw.QComboBox()		
        self.comboBox_design_observe_k_factor_crossing_surface_condition.addItems(list_yes_no)

        self.comboBox_design_observe_k_factor_superelevation = qtw.QComboBox()
        self.comboBox_design_observe_k_factor_superelevation.addItems(list_yes_no)

        self.comboBox_design_observe_k_factor_crossing_nearby_intersection = qtw.QComboBox()
        self.comboBox_design_observe_k_factor_crossing_nearby_intersection.addItems(list_yes_no)
        
        self.comboBox_design_observe_k_factor_vehicle_restrictions = qtw.QComboBox()
        self.comboBox_design_observe_k_factor_vehicle_restrictions.addItems(list_yes_no)

        self.comboBox_design_observe_k_factor_pavement_marking_condition = qtw.QComboBox()
        self.comboBox_design_observe_k_factor_pavement_marking_condition.addItems(list_yes_no)
        
        self.comboBox_design_observe_field_acceleration_times_exceed_td = qtw.QComboBox()
        self.comboBox_design_observe_field_acceleration_times_exceed_td.addItems(list_yes_no)

        self.comboBox_design_road_design_vehicle_type = qtw.QComboBox()
        self.comboBox_design_road_design_vehicle_type.addItems(list_design_road_design_vehicle_type)

        #Group Labels
        self.label_design_calculate_adjacent_track_clearance_time = qtw.QLabel('No Value')
        self.label_design_calculate_clearance_time_pedestrian_design_check = qtw.QLabel('No Value')
        self.label_design_calculate_clearance_time_vehicle_design_check = qtw.QLabel('No Value')
        self.label_design_calculate_gate_arm_clearance_time_pedestrian = qtw.QLabel('No Value')
        self.label_design_calculate_gate_arm_clearance_time_vehicle_ssd = qtw.QLabel('No Value')
        self.label_design_calculate_gate_arm_clearance_time_vehicle_stop = qtw.QLabel('No Value')
        self.label_design_calculate_gate_arm_clearance_time_vehicle_recommended = qtw.QLabel('No Value')
        self.label_design_calculate_vehicle_departure_time = qtw.QLabel('No Value')
        self.label_design_calculate_vehicle_departure_time_grade_adjusted = qtw.QLabel('No Value')
        self.label_design_calculate_vehicle_departure_time_gate_arm_clearance = qtw.QLabel('No Value')
        self.label_design_calculate_vehicle_departure_time_gate_arm_clearance_grade_adjusted = qtw.QLabel('No Value')

        self.label_design_calculate_vehicle_travel_distance = qtw.QLabel('No Value')
        self.label_design_input_reaction_time = qtw.QLabel()
        self.label_design_input_reaction_time.setNum(2)
        self.label_design_lookup_design_vehicle_class = qtw.QLabel('No Value')
        self.label_design_lookup_design_vehicle_length = qtw.QLabel('No Value')
        self.label_design_lookup_grade_adjustment_factor = qtw.QLabel('No Value')
        self.label_design_measure_clearance_distance_gate_arm_ssd = qtw.QLabel('No Value')
        self.label_design_measure_clearance_distance_gate_arm_stop = qtw.QLabel('No Value')

        # LOCATION OF GRADE CROSSING (GCS SECTION 11)
        #Group TextEdits
        self.textEdit_location_of_grade_crossing_comments = qtw.QTextEdit()

        #Group DoubleSpinBox
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_other_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_other_n_or_e_approach.setRange(0, 999999)

        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_other_s_of_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_other_s_of_w_approach.setRange(0, 999999)

        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach.setRange(0, 999999)
        
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach.setRange(0, 999999)
        
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach.setRange(0, 999999)
        
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach.setRange(0, 999999)

        #group ComboBoxes
        self.comboBox_location_of_grade_crossing_observe_nearby_pedestrian_crosswalk = qtw.QComboBox()
        self.comboBox_location_of_grade_crossing_observe_nearby_pedestrian_crosswalk.addItems(list_yes_no)

        self.comboBox_location_of_grade_crossing_queue_condition = qtw.QComboBox()
        self.comboBox_location_of_grade_crossing_queue_condition.addItems(list_yes_no)

        self.comboBox_location_of_grade_crossing_visibility_of_warning_lights = qtw.QComboBox()
        self.comboBox_location_of_grade_crossing_visibility_of_warning_lights.addItems(list_yes_no)
        
        # GRADE CROSSING SURFACE (GCS SECTION 5)
        #Group TextEdits
        self.textEdit_grade_crossing_surface_comments = qtw.QTextEdit()

        #Group DoubleSpinBox
        self.doubleSpinBox_grade_crossing_surface_measure_crossing_surface_extension_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_crossing_surface_extension_n_or_e_approach.setRange(0, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_crossing_surface_extension_s_or_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_crossing_surface_extension_n_or_e_approach.setRange(0, 999999)

        self.doubleSpinBox_grade_crossing_surface_measure_crossing_surface_width = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_crossing_surface_width.setRange(0, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_n_or_e_approach.setRange(-999999, 999999)

        self.doubleSpinBox_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_s_or_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_s_or_w_approach.setRange(-999999, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_n_or_e_approach.setRange(-999999, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_s_or_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_s_or_w_approach.setRange(-999999, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_elevation_top_of_rail_above_road_surface = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_elevation_top_of_rail_above_road_surface.setRange(-999999, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_elevation_top_of_rail_below_road_surface = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_elevation_top_of_rail_below_road_surface.setRange(-999999, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_flangeway_depth = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_flangeway_depth.setRange(-999999, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_flangeway_width = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_flangeway_width.setRange(-999999, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_median_width = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_median_width.setRange(0, 999999)

        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_shoulder_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_shoulder_n_or_e_approach.setRange(0, 999999)

        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_shoulder_s_or_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_shoulder_s_or_w_approach.setRange(0, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_travel_lanes_width_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_travel_lanes_width_n_or_e_approach.setRange(0, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_travel_lanes_width_s_or_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_travel_lanes_width_s_or_w_approach.setRange(0, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_side_grinding_depth = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_side_grinding_depth.setRange(-999999, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_side_grinding_width = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_side_grinding_width.setRange(-999999, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_extension_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_extension_n_or_e_approach.setRange(0, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_extension_s_or_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_extension_s_or_w_approach.setRange(0, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_width_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_width_n_or_e_approach.setRange(0, 999999)
        
        self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_width_s_or_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_width_s_or_w_approach.setRange(0, 999999)

        #Group ComboBoxes
        self.comboBox_grade_crossing_surface_observe_crossing_smoothness = qtw.QComboBox()
        self.comboBox_grade_crossing_surface_observe_crossing_smoothness.addItems(list_yes_no)

        self.comboBox_grade_crossing_surface_observe_crossing_surface_condition = qtw.QComboBox()
        self.comboBox_grade_crossing_surface_observe_crossing_smoothness.addItems(list_condition)

        self.comboBox_grade_crossing_surface_observe_material = qtw.QComboBox()
        self.comboBox_grade_crossing_surface_observe_material.addItems(list_grade_crossing_surface_observe_material)

        self.comboBox_grade_crossing_surface_observe_road_approach_surface_condition = qtw.QComboBox()
        self.comboBox_grade_crossing_surface_observe_road_approach_surface_condition.addItems(list_condition)

        self.comboBox_grade_crossing_surface_observe_road_approach_surface_type = qtw.QComboBox()
        self.comboBox_grade_crossing_surface_observe_road_approach_surface_type.addItems(list_grade_crossing_surface_observe_road_approach_surface_type)

        # ROAD GEOMETRY (GCS SECTION 6)
        #Group TextEdits 
        self.textEdit_road_geometry_comments = qtw.QTextEdit()

        #Group SpinBox
        self.spinBox_road_geometry_road_crossing_angle = qtw.QSpinBox() 

        #Group DoubleSpinBox
        self.doubleSpinBox_road_geometry_measure_railway_cross_slope = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_road_geometry_measure_railway_cross_slope.setRange(-999999, 999999)

        self.doubleSpinBox_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_n_or_e_approach.setRange(-999999, 999999)
        
        self.doubleSpinBox_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_s_or_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_s_or_w_approach.setRange(-999999, 999999)
        
        self.doubleSpinBox_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_n_or_e_approach.setRange(-999999, 999999)
        
        self.doubleSpinBox_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_s_or_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_s_or_w_approach.setRange(-999999, 999999)
        
        self.doubleSpinBox_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach.setRange(-999999, 999999)
        
        self.doubleSpinBox_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach.setRange(-999999, 999999)
        
        self.doubleSpinBox_road_geometry_rail_superelevation_rate = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_road_geometry_rail_superelevation_rate.setRange(-999999, 999999)
        
        self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.setRange(-999999, 999999)
        
        self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.setRange(-999999, 999999)

        #Group ComboBoxes
        self.comboBox_road_geometry_observe_lane_width_crossing_vs_approach_n_or_e_approach = qtw.QComboBox()
        self.comboBox_road_geometry_observe_lane_width_crossing_vs_approach_n_or_e_approach.addItems(list_yes_no)

        self.comboBox_road_geometry_observe_lane_width_crossing_vs_approach_s_or_w_approach = qtw.QComboBox()
        self.comboBox_road_geometry_observe_lane_width_crossing_vs_approach_s_or_w_approach.addItems(list_yes_no)

        self.comboBox_road_geometry_observe_low_bed_truck_condition = qtw.QComboBox()
        self.comboBox_road_geometry_observe_low_bed_truck_condition.addItems(list_yes_no)

        self.comboBox_road_geometry_observe_smooth_alignment_within_ssd_n_or_e_approach = qtw.QComboBox()
        self.comboBox_road_geometry_observe_smooth_alignment_within_ssd_n_or_e_approach.addItems(list_yes_no)

        self.comboBox_road_geometry_observe_smooth_alignment_within_ssd_s_or_w_approach = qtw.QComboBox()
        self.comboBox_road_geometry_observe_smooth_alignment_within_ssd_s_or_w_approach.addItems(list_yes_no)
       
        self.comboBox_road_geometry_rail_superelevation = qtw.QComboBox() 
        self.comboBox_road_geometry_rail_superelevation.addItems(list_yes_no)

        #Group Labels
        self.label_road_geometry_lookup_gradient_difference = qtw.QLabel('No Value')
        #TBD self.label_road_geometry_observe_gradient_difference_n_or_e_approach = qtw.QLabel('No Value')
        #TBD self.label_road_geometry_observe_gradient_difference_s_or_w_approach = qtw.QLabel('No Value')
        
        # SIGHTLINES (GCS SECTION 7)
        #Group TextEdits
        self.textEdit_sightlines_comments = qtw.QTextEdit()
        
        #Group DoubleSpinBox
        self.doubleSpinBox_sightlines_measure_dssd_actual_n_or_e_approach_left = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_dssd_actual_n_or_e_approach_left.setRange(0, 999999)

        self.doubleSpinBox_sightlines_measure_dssd_actual_n_or_e_approach_right = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_dssd_actual_n_or_e_approach_right.setRange(0, 999999)

        self.doubleSpinBox_sightlines_measure_dssd_actual_s_or_w_approach_left = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_dssd_actual_s_or_w_approach_left.setRange(0, 999999)

        self.doubleSpinBox_sightlines_measure_dssd_actual_s_or_w_approach_right = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_dssd_actual_s_or_w_approach_right.setRange(0, 999999)

        self.doubleSpinBox_sightlines_measure_dstopped_actual_n_or_e_approach_driver_left = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_dstopped_actual_n_or_e_approach_driver_left.setRange(0, 999999)

        self.doubleSpinBox_sightlines_measure_dstopped_actual_n_or_e_approach_driver_right = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_dstopped_actual_n_or_e_approach_driver_right.setRange(0, 999999)

        self.doubleSpinBox_sightlines_measure_dstopped_actual_s_or_w_approach_driver_left = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_dstopped_actual_s_or_w_approach_driver_left.setRange(0, 999999)

        self.doubleSpinBox_sightlines_measure_dstopped_actual_s_or_w_approach_driver_right = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_dstopped_actual_s_or_w_approach_driver_right.setRange(0, 999999)

        self.doubleSpinBox_sightlines_measure_ssd_actual_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_ssd_actual_n_or_e_approach.setRange(0, 999999)

        self.doubleSpinBox_sightlines_measure_ssd_actual_s_or_w_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_ssd_actual_s_or_w_approach.setRange(0, 999999)

        #Group ComboBoxes
        self.comboBox_sightlines_observe_sightline_obstructions = qtw.QComboBox()
        self.comboBox_sightlines_observe_sightline_obstructions.addItems(list_yes_no)

        #Group Labels
        self.label_sightlines_calculate_dssd_vehicle_min_ft = qtw.QLabel('No Value')
        self.label_sightlines_calculate_dssd_vehicle_min_m = qtw.QLabel('No Value')
        self.label_sightlines_calculate_dstopped_pedestrian_min_ft = qtw.QLabel('No Value')
        self.label_sightlines_calculate_dstopped_pedestrian_min_m = qtw.QLabel('No Value')
        self.label_sightlines_calculate_dstopped_vehicle_min_ft = qtw.QLabel('No Value')
        self.label_sightlines_calculate_dstopped_vehicle_min_m = qtw.QLabel('No Value')
        self.label_sightlines_lookup_existing_active_crossing = qtw.QLabel('No Value')
        self.label_sightlines_lookup_existing_active_crossing_with_gates = qtw.QLabel('No Value')
        self.label_sightlines_lookup_ssd_minimum_n_or_e_approach = qtw.QLabel('No Value')
        self.label_sightlines_lookup_ssd_minimum_s_or_w_approach = qtw.QLabel('No Value')

        # SIGNS AND PAVEMENT MARKINGS (GCS SECTION 8)
        #Group TextEdits
        #DELETE self.textEdit_signs_and_markings_advisory_speed_comments = pass
        #DELETE self.textEdit_signs_and_markings_comments = pass
        #DELETE self.textEdit_signs_and_markings_emergency_notification_comments = pass
        #DELETE self.textEdit_signs_and_markings_number_of_tracks_comments = pass
        #DELETE self.textEdit_signs_and_markings_railway_crossing_ahead_comments = pass
        #DELETE self.textEdit_signs_and_markings_railway_crossing_comments = pass
        #DELETE self.textEdit_signs_and_markings_stop_comments = pass
        #DELETE self.textEdit_signs_and_markings_stop_sign_ahead_comments = pass

        #Group DoubleSpinBox
        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_rail.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_road.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_height.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_rail.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_road.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_height.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_stop_n_or_e_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_n_or_e_approach_height.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_stop_n_or_e_approach_location_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_n_or_e_approach_location_from_rail.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_stop_n_or_e_approach_location_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_n_or_e_approach_location_from_road.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_stop_s_or_w_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_s_or_w_approach_height.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_stop_s_or_w_approach_location_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_s_or_w_approach_location_from_rail.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_stop_s_or_w_approach_location_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_s_or_w_approach_location_from_road.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_height.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_rail.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_road.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_height.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_rail.setRange(0, 999999)

        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_road.setRange(0, 999999)
        
        #Group ComboBoxes
        self.comboBox_signs_and_markings_advisory_speed_n_or_e_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_advisory_speed_n_or_e_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_advisory_speed_n_or_e_approach_with_wa_18_20 = qtw.QComboBox()
        self.comboBox_signs_and_markings_advisory_speed_n_or_e_approach_with_wa_18_20.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_advisory_speed_s_or_w_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_advisory_speed_s_or_w_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_advisory_speed_s_or_w_approach_with_wa_18_20 = qtw.QComboBox()
        self.comboBox_signs_and_markings_advisory_speed_s_or_w_approach_with_wa_18_20.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_dividing_lines_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_dividing_lines_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_condition = qtw.QComboBox()
        self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_condition.addItems(list_condition)

        self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_legible = qtw.QComboBox()
        self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_legible.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_orientation = qtw.QComboBox()
        self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_orientation.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_condition = qtw.QComboBox()
        self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_condition.addItems(list_condition)

        self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_legible = qtw.QComboBox()
        self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_legible.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_orientation = qtw.QComboBox()
        self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_orientation.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_1b = qtw.QComboBox()
        self.comboBox_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_1b.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_3c = qtw.QComboBox()
        self.comboBox_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_3c.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_number_of_tracks_n_or_e_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_number_of_tracks_n_or_e_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_1b = qtw.QComboBox()
        self.comboBox_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_1b.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_3c = qtw.QComboBox()
        self.comboBox_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_3c.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_number_of_tracks_s_or_w_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_number_of_tracks_s_or_w_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_per_mutcd = qtw.QComboBox()
        self.comboBox_signs_and_markings_per_mutcd.addItems(list_yes_no)

        self.comboBox_signs_and_markings_posted_speed_n_or_e_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_posted_speed_n_or_e_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_posted_speed_s_or_w_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_posted_speed_s_or_w_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_orientation = qtw.QComboBox()
        self.comboBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_orientation.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_orientation = qtw.QComboBox()
        self.comboBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_orientation.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_railway_crossing_n_or_e_approach_per_fig_8_1a = qtw.QComboBox()
        self.comboBox_signs_and_markings_railway_crossing_n_or_e_approach_per_fig_8_1a.addItems(list_yes_no)

        self.comboBox_signs_and_markings_railway_crossing_n_or_e_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_railway_crossing_n_or_e_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_railway_crossing_s_or_w_approach_per_fig_8_1a = qtw.QComboBox()
        self.comboBox_signs_and_markings_railway_crossing_s_or_w_approach_per_fig_8_1a.addItems(list_yes_no)

        self.comboBox_signs_and_markings_railway_crossing_s_or_w_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_railway_crossing_s_or_w_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_sidewalks_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_sidewalks_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_stop_n_or_e_approach_per_fig_8_4 = qtw.QComboBox()
        self.comboBox_signs_and_markings_stop_n_or_e_approach_per_fig_8_4.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_stop_n_or_e_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_stop_n_or_e_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_stop_n_or_e_approach_same_post = qtw.QComboBox()
        self.comboBox_signs_and_markings_stop_n_or_e_approach_same_post.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_stop_s_or_w_approach_per_fig_8_4 = qtw.QComboBox()
        self.comboBox_signs_and_markings_stop_s_or_w_approach_per_fig_8_4.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_stop_s_or_w_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_stop_s_or_w_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_stop_s_or_w_approach_same_post = qtw.QComboBox()
        self.comboBox_signs_and_markings_stop_s_or_w_approach_same_post.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_present.addItems(list_yes_no)

        # GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)
        #Group TextEdits
        self.textEdit_gcws_warrants_comments = qtw.QTextEdit()
        
        # Group Labels
        self.label_gcws_warrant_private_9_3 = qtw.QLabel('No Value')
        self.label_gcws_warrant_private_9_3_1 = qtw.QLabel('No Value')
        self.label_gcws_warrant_private_9_3_2_a = qtw.QLabel('No Value')
        self.label_gcws_warrant_private_9_3_2_b = qtw.QLabel('No Value')
        self.label_gcws_warrant_private_9_3_2_c = qtw.QLabel('No Value')
        self.label_gcws_warrant_public_9_1 = qtw.QLabel('No Value')
        self.label_gcws_warrant_public_9_1_a = qtw.QLabel('No Value')
        self.label_gcws_warrant_public_9_1_b = qtw.QLabel('No Value')
        self.label_gcws_warrant_public_9_1_c = qtw.QLabel('No Value')
        self.label_gcws_warrant_public_9_1_d_i = qtw.QLabel('No Value')
        self.label_gcws_warrant_public_9_1_d_ii = qtw.QLabel('No Value')
        self.label_gcws_warrant_public_9_1_d_iii = qtw.QLabel('No Value')
        self.label_gcws_warrant_sidewalk_9_5 = qtw.QLabel('No Value')
        self.label_gates_gcws_warrant_private_9_4_1_a = qtw.QLabel('No Value')
        self.label_gates_gcws_warrant_private_9_4_1_b = qtw.QLabel('No Value')
        self.label_gates_gcws_warrant_private_9_4_1_c = qtw.QLabel('No Value')
        self.label_gates_gcws_warrant_public_9_2_1_a = qtw.QLabel('No Value')
        self.label_gates_gcws_warrant_public_9_2_1_b = qtw.QLabel('No Value')
        self.label_gates_gcws_warrant_public_9_2_1_c = qtw.QLabel('No Value')
        self.label_gates_gcws_warrant_public_9_2_1_d = qtw.QLabel('No Value')
        self.label_gates_gcws_warrant_public_9_2_1_e = qtw.QLabel('No Value')
        self.label_gates_gcws_warrant_sidewalk_9_6 = qtw.QLabel('No Value')

        # GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)
        #Group TextEdits
        self.textEdit_gcws_comments = qtw.QTextEdit()
        
        #Group SpinBox
        self.spinBox_gcws_rail_design_warning_time_preemption = qtw.QSpinBox()
        self.spinBox_gcws_rail_design_warning_time_preemption.setRange(0, 999999)
        
        #Group DoubleSpinBox
        self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_distance_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_distance_from_rail.setRange(0, 999999)
        
        self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_distance_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_distance_from_road.setRange(0, 999999)
        
        self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_distance_top_of_foundation = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_distance_top_of_foundation.setRange(0, 999999)
        
        self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_slope_from_foundation = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_slope_from_foundation.setRange(0, 999999)
        
        self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_distance_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_distance_from_rail.setRange(0, 999999)
        
        self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_distance_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_distance_from_road.setRange(0, 999999)
        
        self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_distance_top_of_foundation = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_distance_top_of_foundation.setRange(0, 999999)
        
        self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_slope_from_foundation = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_slope_from_foundation.setRange(0, 999999)
        
        self.doubleSpinBox_gcws_rail_crossing_warning_time_actual = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gcws_rail_crossing_warning_time_actual.setRange(0, 999999)
        
        #Group ComboBox
        self.comboBox_gcws_observe_bell_if_sidewalk = qtw.QComboBox()
        self.comboBox_gcws_observe_bell_if_sidewalk.addItems(list_yes_no)

        self.comboBox_gcws_observe_bells_condition = qtw.QComboBox()
        self.comboBox_gcws_observe_bells_condition.addItems(list_condition)

        self.comboBox_gcws_observe_bells_n_or_e_approach = qtw.QComboBox()
        self.comboBox_gcws_observe_bells_n_or_e_approach.addItems(list_yes_no)

        self.comboBox_gcws_observe_bells_s_or_w_approach = qtw.QComboBox()
        self.comboBox_gcws_observe_bells_s_or_w_approach.addItems(list_yes_no)

        self.comboBox_gcws_observe_cantilever_lights_condition = qtw.QComboBox()
        self.comboBox_gcws_observe_cantilever_lights_condition.addItems(list_condition)

        self.comboBox_gcws_observe_cantilever_lights_n_or_e_approach = qtw.QComboBox()
        self.comboBox_gcws_observe_cantilever_lights_n_or_e_approach.addItems(list_yes_no)

        self.comboBox_gcws_observe_cantilever_lights_s_or_w_approach = qtw.QComboBox()
        self.comboBox_gcws_observe_cantilever_lights_s_or_w_approach.addItems(list_yes_no)

        self.comboBox_gcws_observe_gates_condition = qtw.QComboBox()
        self.comboBox_gcws_observe_gates_condition.addItems(list_condition)

        self.comboBox_gcws_observe_gates_n_or_e_approach = qtw.QComboBox()
        self.comboBox_gcws_observe_gates_n_or_e_approach.addItems(list_yes_no)

        self.comboBox_gcws_observe_gates_s_or_w_approach = qtw.QComboBox()
        self.comboBox_gcws_observe_gates_s_or_w_approach.addItems(list_yes_no)

        self.comboBox_gcws_observe_gcws_limited_use_with_walk_light_assembly = qtw.QComboBox()
        self.comboBox_gcws_observe_gcws_limited_use_with_walk_light_assembly.addItems(list_yes_no_na)

        self.comboBox_gcws_observe_gcws_limited_use_without_walk_light_assembly = qtw.QComboBox()
        self.comboBox_gcws_observe_gcws_limited_use_without_walk_light_assembly.addItems(list_yes_no_na)

        self.comboBox_gcws_observe_light_units_condition = qtw.QComboBox()
        self.comboBox_gcws_observe_light_units_condition.addItems(list_condition)

        self.comboBox_gcws_observe_light_units_n_or_e_approach = qtw.QComboBox()
        self.comboBox_gcws_observe_light_units_n_or_e_approach.addItems(list_yes_no)

        self.comboBox_gcws_observe_light_units_s_or_w_approach = qtw.QComboBox()
        self.comboBox_gcws_observe_light_units_s_or_w_approach.addItems(list_yes_no)

        self.comboBox_gcws_observe_warning_time_consistency = qtw.QComboBox()
        self.comboBox_gcws_observe_warning_time_consistency.addItems(list_yes_no_na)
        
        self.comboBox_gcws_observe_warning_time_consistency_reduced_speed = qtw.QComboBox()
        self.comboBox_gcws_observe_warning_time_consistency_reduced_speed.addItems(list_yes_no_na)

        self.comboBox_gcws_rail_cut_out_circuit_requirements = qtw.QComboBox()
        self.comboBox_gcws_rail_cut_out_circuit_requirements.addItems(list_yes_no_na)

        self.comboBox_gcws_rail_directional_stick_circuit_requirements = qtw.QComboBox()
        self.comboBox_gcws_rail_directional_stick_circuit_requirements.addItems(list_yes_no_na)

        self.comboBox_gcws_rail_self_diagnostic = qtw.QComboBox()
        self.comboBox_gcws_rail_self_diagnostic.addItems(list_yes_no_na)

        #Group Labels
        self.label_gcws_rail_design_approach_warning_time = qtw.QLabel('No Value')
        self.label_gcws_rail_design_warning_time_ssd = qtw.QLabel('No Value')
        self.label_gcws_rail_design_warning_time_adjacent_crossing = qtw.QLabel('No Value')
        self.label_gcws_rail_design_warning_time_clearance_distance = qtw.QLabel('No Value')
        self.label_gcws_rail_design_warning_time_departure_time_pedestrian = qtw.QLabel('No Value')
        self.label_gcws_rail_design_warning_time_departure_time_vehicle = qtw.QLabel('No Value')
        self.label_gcws_rail_design_warning_time_gate_arm_clearance = qtw.QLabel('No Value')
        self.label_gcws_rail_design_warning_time_ssd = qtw.QLabel('No Value')

        # FLASHING LIGHT UNITS (GCS SECTION 13 & 14)
        #Group TextEdits
        self.textEdit_light_units_comments = qtw.QTextEdit()

        #Group DoubleSpinBox
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_distance_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_distance_from_rail.setRange(0, 999999)
        
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_distance_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_distance_from_road.setRange(0, 999999)
        
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_dl = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_dl.setRange(0, 999999)
        
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_dr = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_dr.setRange(0, 999999)
        
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_height.setRange(0, 999999)
        
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_distance_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_distance_from_rail.setRange(0, 999999)
        
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_distance_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_distance_from_road.setRange(0, 999999)
        
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_dl = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_dl.setRange(0, 999999)
        
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_dr = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_dr.setRange(0, 999999)
        
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_height.setRange(0, 999999)
        
        self.doubleSpinBox_light_units_measure_n_or_e_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_light_units_measure_n_or_e_approach_height.setRange(0, 999999)
        
        self.doubleSpinBox_light_units_measure_s_or_w_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_light_units_measure_s_or_w_approach_height.setRange(0, 999999)
        
        #Group ComboBoxes
        self.comboBox_light_units_observe_cantilevers_per_fig_12_3 = qtw.QComboBox()
        self.comboBox_light_units_observe_cantilevers_per_fig_12_3.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_per_fig_12_1 = qtw.QComboBox()
        self.comboBox_light_units_observe_per_fig_12_1.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_sidewalks_n_or_e_approach = qtw.QComboBox()
        self.comboBox_light_units_observe_sidewalks_n_or_e_approach.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_sidewalks_s_or_w_approach = qtw.QComboBox()
        self.comboBox_light_units_observe_sidewalks_s_or_w_approach.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_supplemental_lights_n_or_e_approach = qtw.QComboBox()
        self.comboBox_light_units_observe_supplemental_lights_n_or_e_approach.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_supplemental_lights_s_or_w_approach = qtw.QComboBox()
        self.comboBox_light_units_observe_supplemental_lights_s_or_w_approach.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_visibility_back_lights_n_or_e_approach = qtw.QComboBox()
        self.comboBox_light_units_observe_visibility_back_lights_n_or_e_approach.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_visibility_back_lights_s_or_w_approach = qtw.QComboBox()
        self.comboBox_light_units_observe_visibility_back_lights_s_or_w_approach.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_visibility_front_lights_n_or_e_approach = qtw.QComboBox()
        self.comboBox_light_units_observe_visibility_front_lights_n_or_e_approach.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_visibility_front_lights_s_or_w_approach = qtw.QComboBox()
        self.comboBox_light_units_observe_visibility_front_lights_s_or_w_approach.addItems(list_yes_no_na)

        # GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)
        #Group TextEdits
        self.textEdit_gates_gcws_comments = qtw.QTextEdit()

        #Group DoubleSpinBox
        self.doubleSpinBox_gates_gcws_measure_gate_ascent_time = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gates_gcws_measure_gate_ascent_time.setRange(0, 999999)
        
        self.doubleSpinBox_gates_gcws_measure_gate_descent_time = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gates_gcws_measure_gate_descent_time.setRange(0, 999999)
        
        self.doubleSpinBox_gates_gcws_rail_gate_arm_delay_time_design = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gates_gcws_rail_gate_arm_delay_time_design.setRange(0, 999999)
        
        self.doubleSpinBox_gates_gcws_rail_gate_arm_descent_time_design = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gates_gcws_rail_gate_arm_descent_time_design.setRange(0, 999999)
        
        self.doubleSpinBox_gates_gcws_rail_inner_gate_arm_delay_time_design = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gates_gcws_rail_inner_gate_arm_delay_time_design.setRange(0, 999999)
        
        #Group DoubleSpinBox
        self.doubleSpinBox_gates_gcws_measure_distance_between_gate_end_and_road_cl_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_gates_gcws_measure_distance_between_gate_end_and_road_cl_s_or_w_approach = qtw.QDoubleSpinBox() 

        #Group Labels
        self.label_gates_gcws_calculate_inner_gate_arm_delay_time_recommended = qtw.QLabel('No Value')

        #Group ComboBoxes
        self.comboBox_gates_gcws_observe_gate_arm_rest = qtw.QComboBox()
        self.comboBox_gates_gcws_observe_gate_arm_rest.addItems(list_yes_no_na)

        self.comboBox_gates_gcws_observe_gate_ascent_time = qtw.QComboBox()
        self.comboBox_gates_gcws_observe_gate_ascent_time.addItems(list_yes_no_na)

        self.comboBox_gates_gcws_observe_gate_descent_time = qtw.QComboBox()
        self.comboBox_gates_gcws_observe_gate_descent_time.addItems(list_yes_no_na)

        self.comboBox_gates_gcws_observe_gate_strips_n_or_e_approach = qtw.QComboBox()
        self.comboBox_gates_gcws_observe_gate_strips_n_or_e_approach.addItems(list_yes_no_na)

        self.comboBox_gates_gcws_observe_gate_strips_s_or_w_approach = qtw.QComboBox()
        self.comboBox_gates_gcws_observe_gate_strips_s_or_w_approach.addItems(list_yes_no_na)

        self.comboBox_gates_gcws_observe_per_fig_12_2 = qtw.QComboBox()
        self.comboBox_gates_gcws_observe_per_fig_12_2.addItems(list_yes_no_na)

        # PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)
        #Group Text Edits
        self.textEdit_aawd_comments = qtw.QTextEdit()

        #Group DoubleSpinBox
        self.doubleSpinBox_aawd_measure_distance_sign_and_stop_n_or_e_approach_actual = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_aawd_measure_distance_sign_and_stop_n_or_e_approach_actual.setRange(0, 999999)

        self.doubleSpinBox_aawd_measure_distance_sign_and_stop_s_or_w_approach_actual = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_aawd_measure_distance_sign_and_stop_s_or_w_approach_actual.setRange(0, 999999)

        #Group ComboBoxes
        self.comboBox_aawd_observe_present_n_or_e_approach = qtw.QComboBox()
        self.comboBox_aawd_observe_present_n_or_e_approach.addItems(list_yes_no)

        self.comboBox_aawd_observe_present_s_or_w_approach = qtw.QComboBox()
        self.comboBox_aawd_observe_present_s_or_w_approach.addItems(list_yes_no)

        self.comboBox_aawd_road_aawd_sufficient_activation_time_n_or_e_approach = qtw.QComboBox()
        self.comboBox_aawd_road_aawd_sufficient_activation_time_n_or_e_approach.addItems(list_yes_no_na)

        self.comboBox_aawd_road_aawd_sufficient_activation_time_s_or_w_approach = qtw.QComboBox()
        self.comboBox_aawd_road_aawd_sufficient_activation_time_s_or_w_approach.addItems(list_yes_no_na)

        self.comboBox_aawd_warrant_gcr_observe_environmental_condition = qtw.QComboBox()
        self.comboBox_aawd_road_aawd_sufficient_activation_time_n_or_e_approach.addItems(list_yes_no_na)

        self.comboBox_aawd_warrant_gcr_observe_sightline_obstruction = qtw.QComboBox()
        self.comboBox_aawd_road_aawd_sufficient_activation_time_n_or_e_approach.addItems(list_yes_no_na)

        self.comboBox_aawd_warrant_mutcd_lookup_significant_road_downgrade = qtw.QComboBox()
        self.comboBox_aawd_road_aawd_sufficient_activation_time_n_or_e_approach.addItems(list_yes_no_na)

        #Group Labels
        self.label_aawd_calculate_advance_activation_time_design_n_or_e_approach = qtw.QLabel('No Value')
        self.label_aawd_calculate_advance_activation_time_design_s_or_w_approach = qtw.QLabel('No Value')
        self.label_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended = qtw.QLabel('No Value')
        self.label_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended = qtw.QLabel('No Value')
        self.label_aawd_warrant_gcr_lookup_road_classification = qtw.QLabel('No Value')
        self.label_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr = qtw.QLabel('No Value')
        
        # INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)
        #Group TextEdits
        self.textEdit_preemption_of_traffic_signals_comments = qtw.QTextEdit()
    
        #Group SpinBox
        self.spinBox_preemption_of_traffic_signals_road_preemption_warning_time_actual = qtw.QSpinBox() 
        self.spinBox_preemption_of_traffic_signals_road_preemption_warning_time_design = qtw.QSpinBox() 

        #Group CombBoxes
        self.comboBox_preemption_of_traffic_signals_observe_consideration_of_Longer_vehicles = qtw.QComboBox()
        self.comboBox_preemption_of_traffic_signals_observe_consideration_of_Longer_vehicles.addItems(list_yes_no)

        self.comboBox_preemption_of_traffic_signals_observe_known_queuing_issues = qtw.QComboBox()
        self.comboBox_preemption_of_traffic_signals_observe_known_queuing_issues.addItems(list_yes_no)

        self.comboBox_preemption_of_traffic_signals_observe_pedestrian_accommodation = qtw.QComboBox()
        self.comboBox_preemption_of_traffic_signals_observe_pedestrian_accommodation.addItems(list_yes_no_na)

        self.comboBox_preemption_of_traffic_signals_observe_queuing_condition = qtw.QComboBox()
        self.comboBox_preemption_of_traffic_signals_observe_queuing_condition.addItems(list_yes_no)

        self.comboBox_preemption_of_traffic_signals_observe_supplemental_signage = qtw.QComboBox()
        self.comboBox_preemption_of_traffic_signals_observe_supplemental_signage.addItems(list_yes_no_na)

        self.comboBox_preemption_of_traffic_signals_observe_traffic_clearance_time_adequate = qtw.QComboBox()
        self.comboBox_preemption_of_traffic_signals_observe_traffic_clearance_time_adequate.addItems(list_yes_no_na)

        self.comboBox_preemption_of_traffic_signals_observe_unintended_queuing_by_traffic_signals = qtw.QComboBox()
        self.comboBox_preemption_of_traffic_signals_observe_unintended_queuing_by_traffic_signals.addItems(list_yes_no_na)

        self.comboBox_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type = qtw.QComboBox()
        self.comboBox_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type.addItems(list_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type)

        #Group DatePicker
        #TODO self.label_preemption_of_traffic_signals_road_date_Last_preemption_check = pass

        #Group Labels
        self.label_preemption_of_traffic_signals_lookup_proximity_condition = qtw.QLabel('No Value')
        self.label_preemption_of_traffic_signals_lookup_required = qtw.QLabel('No Value')

        # WHISTLE CESSATION (GCS SECTION Appendix D)
        #Group TextEdits
        self.textEdit_areas_without_train_whistling_comments = qtw.QTextEdit()

        #Group ComboBoxes
        self.comboBox_areas_without_train_whistling_lookup_gcs_12_to_16 = qtw.QComboBox()
        self.comboBox_areas_without_train_whistling_lookup_gcs_12_to_16.addItems(list_yes_no_na)

        self.comboBox_areas_without_train_whistling_observe_for_stop_and_proceed = qtw.QComboBox()
        self.comboBox_areas_without_train_whistling_observe_for_stop_and_proceed.addItems(list_yes_no_na)

        self.comboBox_areas_without_train_whistling_observe_trespassing_area = qtw.QComboBox()
        self.comboBox_areas_without_train_whistling_observe_trespassing_area.addItems(list_yes_no)

        self.comboBox_areas_without_train_whistling_rail_anti_whistling_zone = qtw.QComboBox()
        self.comboBox_areas_without_train_whistling_rail_anti_whistling_zone.addItems(list_yes_no)

        self.comboBox_areas_without_train_whistling_rail_anti_whistling_zone_24_hrs = qtw.QComboBox()
        self.comboBox_areas_without_train_whistling_rail_anti_whistling_zone_24_hrs.addItems(list_yes_no)        

        #Group Labels
        self.label_areas_without_train_whistling_lookup_gcs_9_2 = qtw.QLabel('No Value')
        self.label_areas_without_train_whistling_requirements_lookup_table_d1_criteria = qtw.QLabel('No Value')
        self.label_areas_without_train_whistling_requirements_observe_table_D1 = qtw.QLabel('No Value')
        
        ##################
        # Layout Objects #
        ##################
        main_layout = qtw.QGridLayout()
        toolbox = qtw.QToolBox()
        self.setLayout(main_layout)
        main_layout.addWidget(toolbox, 0, 0)

        styleSheet = """
                        QToolBox::tab {
                            border: 1px solid #C4C4C3;
                            border-bottom-color: RGB(0, 0, 255);
                        }

                        QToolBox::tab:selected {
                            background-color: #f14040;
                            border-bottom-style: none;
                        }
                     """ 

        # QWidgets - Create a container widget
        container_general = qtw.QWidget(self)
        container_location_and_classification_info = qtw.QWidget(self)
        container_railroad_info = qtw.QWidget(self)
        container_traffic_control_device_info = qtw.QWidget(self)
        container_physical_characteristics = qtw.QWidget(self)
        container_hwy_info = qtw.QWidget(self)

        #QFormLayout - Create a form layout
        form_layout_general = qtw.QFormLayout()
        form_layout_location_and_classification_info = qtw.QFormLayout()
        form_layout_railroad_info = qtw.QFormLayout()
        form_layout_traffic_control_device_info = qtw.QFormLayout()
        form_layout_physical_characteristics = qtw.QFormLayout()
        form_layout_hwy_info = qtw.QFormLayout()

        #Set Form Layouts to Container Widgets
        container_general.setLayout(form_layout_general)        
        container_location_and_classification_info.setLayout(form_layout_location_and_classification_info)
        container_railroad_info.setLayout(form_layout_railroad_info)
        container_traffic_control_device_info.setLayout(form_layout_traffic_control_device_info)
        container_physical_characteristics.setLayout(form_layout_physical_characteristics)
        container_hwy_info.setLayout(form_layout_hwy_info)

        #Add Container Widgets to Toolbox
        toolbox.addItem(container_general, 'GENERAL DETAILS')
        toolbox.addItem(container_location_and_classification_info, 'PART I: LOCATION AND CLASSIFICATION INFORMATION')
        toolbox.addItem(container_railroad_info, 'PART II: RAILROAD INFORMATION')
        toolbox.addItem(container_traffic_control_device_info, 'PART III: TRAFFIC CONTROL DEVICE INFORMATION')
        toolbox.addItem(container_physical_characteristics, 'PART IV: PHYSICAL CHARACTERISTICS')
        toolbox.addItem(container_hwy_info, 'PART V: HIGHWAY INFORMATION')
        
        toolbox.setCurrentIndex(0)
        toolbox.setStyleSheet(styleSheet)
        
        # layout container widgets - GENERAL DETAILS
        form_layout_general.addRow(qtw.QLabel('TBD'))
        form_layout_general.addRow('TBD:', self.TBD_Widget)
        

        # layout container widgets - PART I: LOCATION AND CLASSIFICATION INFORMATION
        form_layout_location_and_classification_info.addRow(qtw.QLabel('TBD'))
        form_layout_location_and_classification_info.addRow('TBD:', self.TBD_Widget)
        
        # layout container widgets - PART II: RAILROAD INFORMATION
        form_layout_railroad_info.addRow(qtw.QLabel('TBD'))
        form_layout_railroad_info.addRow('TBD:', self.TBD_Widget)
        
        # layout container widgets - PART III: TRAFFIC CONTROL DEVICE INFORMATION
        form_layout_traffic_control_device_info.addRow(qtw.QLabel('TBD'))
        form_layout_traffic_control_device_info.addRow('TBD:', self.TBD_Widget)
        
        # layout container widgets - PART IV: PHYSICAL CHARACTERISTICS
        form_layout_physical_characteristics.addRow(qtw.QLabel('TBD'))
        form_layout_physical_characteristics.addRow('TBD:', self.TBD_Widget)

        # layout container widgets - PART V: HIGHWAY INFORMATION
        container_hwy_info.addRow(qtw.QLabel('TBD'))
        container_hwy_info.addRow('TBD:', self.TBD_Widget)

        '''
        #######################
        # Size Control Layout #
        #######################

        # use stretch factor

        stretch_layout = qtw.QHBoxLayout()
        main_layout.addLayout(stretch_layout)
        stretch_layout.addWidget(qtw.QLineEdit('Short'), 1)
        stretch_layout.addWidget(qtw.QLineEdit('Long'), 2)
        
        ######################
        # The central widget #
        ######################
        self.textedit = qtw.QTextEdit()
        self.setCentralWidget(self.textedit)

        #################
        # The Statusbar #
        #################

        # The long way 'round
        #status_bar = qtw.QStatusBar()
        #self.setStatusBar(status_bar)
        #status_bar.showMessage('Welcome to text_editor.py')

        # The short way 'round
        self.statusBar().showMessage('Welcome to text_editor.py')

        # add widgets to statusbar
        charcount_self.label = qtw.QLabel("chars: 0")
        self.textedit.textChanged.connect(
            lambda: charcount_self.label.setText(
                "chars: " +
                str(len(self.textedit.toPlainText()))
                )
            )
        self.statusBar().addPermanentWidget(charcount_self.label)

        ###############j
        # The menubar #
        ###############
        menubar = self.menuBar()

        # add submenus to a menu
        file_menu = menubar.addMenu('File')
        edit_menu = menubar.addMenu('Edit')
        help_menu = menubar.addMenu('Help')

        # add actions
        open_action = file_menu.addAction('Open')
        save_action = file_menu.addAction('Save')

        # add separator
        file_menu.addSeparator()

        # add an action with a callback
        # Errata:  The book contains this line:
        #quit_action = file_menu.addAction('Quit', self.destroy)
        # It should call self.close instead, like so:
        quit_action = file_menu.addAction('Quit', self.close)

        # connect to a Qt Slot
        edit_menu.addAction('Undo', self.textedit.undo)

        # create a QAction manually

        redo_action = qtw.QAction('Redo', self)
        redo_action.triggered.connect(self.textedit.redo)
        edit_menu.addAction(redo_action)

        ############################
        # The Toolbar and QActions #
        ############################

        toolbar = self.addToolBar('File')
        #toolbar.addAction(open_action)
        #toolbar.addAction("Save")

        toolbar.setMovable(False)
        toolbar.setFloatable(False)
        toolbar.setAllowedareas(
            qtc.Qt.topToolBararea |
            qtc.Qt.BottomToolBararea
        )

        # Add with icons
        open_icon = self.style().standardIcon(qtw.QStyle.SP_DirOpenIcon)
        save_icon = self.style().standardIcon(qtw.QStyle.SP_DriveHDIcon)

        open_action.setIcon(open_icon)
        toolbar.addAction(open_action)
        toolbar.addAction(
            save_icon,
            'Save',
            lambda: self.statusBar().showMessage('File Saved!')
        )

        # create a custom QAction

        help_action = qtw.QAction(
            self.style().standardIcon(qtw.QStyle.SP_DialogHelpButton),
            'Help',
            self,  # important to pass the parent!
            triggered=lambda: self.statusBar().showMessage(
                'Sorry, no help yet!'
            )
        )
        toolbar.addAction(help_action)

        # create a toolbar in another part of the screen:
        toolbar2 = qtw.QToolBar('Edit')
        self.addToolBar(qtc.Qt.RightToolBararea, toolbar2)
        toolbar2.addAction('Copy', self.textedit.copy)
        toolbar2.addAction('Cut', self.textedit.cut)
        toolbar2.addAction('Paste', self.textedit.paste)


        ################
        # Dock Widgets #
        ################

        dock = qtw.QDockWidget("Replace")
        self.addDockWidget(qtc.Qt.LeftDockWidgetarea, dock)

        # make it not closable
        dock.setFeatures(
            qtw.QDockWidget.DockWidgetMovable |
            qtw.QDockWidget.DockWidgetFloatable
        )

        replace_widget = qtw.QWidget()
        replace_widget.setLayout(qtw.QVBoxLayout())
        dock.setWidget(replace_widget)

        self.search_text_inp = qtw.QLineEdit(placeholderText='search')
        self.replace_text_inp = qtw.QLineEdit(placeholderText='replace')
        search_and_replace_btn = qtw.QPushButton(
            "Search and Replace",
            clicked=self.search_and_replace
            )
        replace_widget.layout().addRow(input_self.search_text_inp)
        replace_widget.layout().addRow(input_self.replace_text_inp)
        replace_widget.layout().addRow(input_search_and_replace_btn)
        replace_widget.layout().addStretch()

        ############################
        # Messageboxes and Dialogs #
        ############################

        # QMessageBox
        help_menu.addAction('About', self.showAboutDialog)

        if self.settings.value('show_warnings', False, type=bool):
            response = qtw.QMessageBox.question(
                self,
                'My Text Editor',
                'This is beta software, do you want to continue?',
                qtw.QMessageBox.Yes | qtw.QMessageBox.Abort
            )
            if response == qtw.QMessageBox.Abort:
                self.close()
                sys.exit()

            # custom message box

            splash_screen = qtw.QMessageBox()
            splash_screen.setWindowTitle('My Text Editor')
            splash_screen.setText('BETA SOFTWARE WARNING!')
            splash_screen.setInformativeText(
                'This is very, very beta, '
                'are you really sure you want to use it?'
            )
            splash_screen.setDetailedText(
                'This editor was written for pedagogical '
                'purposes, and probably is not fit for real work.'
            )
            splash_screen.setWindowModality(qtc.Qt.WindowModal)
            splash_screen.addButton(qtw.QMessageBox.Yes)
            splash_screen.addButton(qtw.QMessageBox.Abort)
            response = splash_screen.exec_()
            if response == qtw.QMessageBox.Abort:
                self.close()
                sys.exit()

        # QFileDialog
        open_action.triggered.connect(self.openFile)
        save_action.triggered.connect(self.saveFile)

        # QFontDialog

        edit_menu.addAction('Set Font…', self.set_font)

        # Custom dialog
        edit_menu.addAction('Settings…', self.show_settings)

        ###################
        # Saving Settings #
        ###################


        # end main UI code
        self.show()

    def search_and_replace(self):
        s_text = self.search_text_inp.text()
        r_text = self.replace_text_inp.text()

        if s_text:
            self.textedit.setText(
                self.textedit.toPlainText().replace(s_text, r_text)
                )

    def showAboutDialog(self):
        qtw.QMessageBox.about(
            self,
            "About text_editor.py",
            "This is a text editor written in PyQt5."
        )

    def openFile(self):
        filename, _ = qtw.QFileDialog.getOpenFileName(
            self,
            "Select a text file to open…",
            qtc.QDir.homePath(),
            'Text Files (*.txt) ;;Python Files (*.py) ;;All Files (*)',
            'Python Files (*.py)',
            qtw.QFileDialog.DontUseNativeDialog |
            qtw.QFileDialog.DontResolveSymlinks
        )
        if filename:
            try:
                with open(filename, 'r') as fh:
                    self.textedit.setText(fh.read())
            except Exception as e:
                # Errata:  Book contains the following line:
                #qtw.QMessageBox.critical(f"Could not load file: {e}")
                # It should read like this:
                qtw.QMessageBox.critical(self, f"Could not load file: {e}")

    def saveFile(self):
        filename, _ = qtw.QFileDialog.getSaveFileName(
            self,
            "Select the file to save to…",
            qtc.QDir.homePath(),
            'Text Files (*.txt) ;;Python Files (*.py) ;;All Files (*)'
        )
        if filename:
            try:
                with open(filename, 'w') as fh:
                    fh.write(self.textedit.toPlainText())
            except Exception as e:
                # Errata:  Book contains this line:
                #qtw.QMessageBox.critical(f"Could not save file: {e}")
                # It should read like this:
                qtw.QMessageBox.critical(self, f"Could not load file: {e}")

    def set_font(self):
        current = self.textedit.currentFont()
        font, accepted = qtw.QFontDialog.getFont(
            current,
            self,
            options=(
                qtw.QFontDialog.DontUseNativeDialog |
                qtw.QFontDialog.MonospacedFonts
            )
        )
        if accepted:
            self.textedit.setCurrentFont(font)

    def show_settings(self):

        settings_dialog = SettingsDialog(self.settings, self)
        settings_dialog.exec()
        '''
    
    