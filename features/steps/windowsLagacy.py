import time
from behave import given, when, then
from pywinauto import Application, mouse
from pywinauto.findwindows import ElementNotFoundError
from pywinauto.keyboard import send_keys
from pywinauto.timings import TimeoutError

@given('the Windows Media Player application is started')
def step_impl(context):
    try:
        context.app = Application(backend="uia").start(r'C:\Program Files (x86)\Windows Media Player\wmplayer.exe')
        context.app = Application(backend="uia").connect(title='Windows Media Player Legacy', timeout=5)
    except (ElementNotFoundError, TimeoutError) as e:
        context.app = None
        assert False, f"Error starting or connecting to the application: {e}"

@when('I click on the "{bar_manu}" tree item')
def step_impl(context, bar_manu):
    if context.app:
        try:
            context.videos_tree_item = context.app.WindowsMediaPlayerLegacy.child_window(title=bar_manu, control_type="TreeItem").wrapper_object()
            context.videos_tree_item.click_input()
        except ElementNotFoundError as e:
            assert False, f"Element not found: {e}"
        except TimeoutError as e:
            assert False, f"Operation timed out: {e}"
        except Exception as e:
            assert False, f"An unexpected error occurred: {e}"
    else:
        assert False, "Application is not started"

@then('I click on the "{media_file}" list item')
def step_double_click_media_file(context, media_file):
    if context.app:
        try:
            # if media_file == "Videos":
            #     media_file_item = context.app.WindowsMediaPlayerLegacy.child_window(title=media_file,
            #                                                                         control_type="ListItem").wrapper_object()
            #     media_file_item.double_click_input()
            media_file_item = context.app.WindowsMediaPlayerLegacy.child_window(title=media_file,
                                                                                    control_type="Text").wrapper_object()
            media_file_item.click_input()

        except ElementNotFoundError as e:
            assert False, f"Element not found: {e}"
        except TimeoutError as e:
            assert False, f"Operation timed out: {e}"
        except Exception as e:
            assert False, f"An unexpected error occurred: {e}"
    else:
        assert False, "Application is not started"

@then('the application should be interacted with successfully')
def step_impl(context):
    assert context.app is not None, "Application is not started"
    print("Application was interacted with successfully")


@then('the application should be closed')
def step_close_application(context):
    if context.app:
        try:
            context.app.kill()  # Close the application
            time.sleep(3)
        except Exception as e:
            assert False, f"Failed to close the application: {e}"



@then('I wait for {duration:d} seconds')
def step_wait_for_duration(context, duration):
    time.sleep(duration)
    # Optionally, you can add logging or print statements for clarity
    print(f"Waited for {duration} seconds.")


@then('I click on the "{media_file}"')
def step_double_click_media_file(context, media_file):
    if context.app:
        try:
            media_file_item = (context.app
                               .WindowsMediaPlayerLegacy
                               .child_window(title=media_file, control_type="ListItem")
                               .wrapper_object())
            media_file_item.click_input()

        except ElementNotFoundError as e:
            assert False, f"Element not found: {e}"
        except TimeoutError as e:
            assert False, f"Operation timed out: {e}"
        except Exception as e:
            assert False, f"An unexpected error occurred: {e}"
    else:
        assert False, "Application is not started"

@then('I click on the play button')
def step_to_click_on_playbutton(context):
    if context.app:
        try:
            media_file_item = (context.app
                               .WindowsMediaPlayerLegacy
                               .child_window(title="Play", control_type="Button", found_index=1)
                               .wrapper_object())
            media_file_item.click_input()

        except ElementNotFoundError as e:
            assert False, f"Element not found: {e}"
        except TimeoutError as e:
            assert False, f"Operation timed out: {e}"
        except Exception as e:
            assert False, f"An unexpected error occurred: {e}"
    else:
        assert False, "Application is not started"


@then('I click on the mute button')
def step_to_click_on_mute_button(context):
    if context.app:
        try:
            media_file_item = (context.app
                               .WindowsMediaPlayerLegacy
                               .child_window(title="Mute", control_type="Button")
                               .wrapper_object())
            media_file_item.click_input()

        except ElementNotFoundError as e:
            assert False, f"Element not found: {e}"
        except TimeoutError as e:
            assert False, f"Operation timed out: {e}"
        except Exception as e:
            assert False, f"An unexpected error occurred: {e}"
    else:
        assert False, "Application is not started"


# @then('I double-click on the MID Sample File')
# def step_double_click_media_file(context, media_file):
#     if context.app:
#         try:
#             media_file_item = (context.app
#                                .WindowsMediaPlayerLegacy
#                                .child_window(title="MID_Sample_File", control_type="ListItem")
#                                .wrapper_object())
#             media_file_item.double_click_input()
#
#         except ElementNotFoundError as e:
#             assert False, f"Element not found: {e}"
#         except TimeoutError as e:
#             assert False, f"Operation timed out: {e}"
#         except Exception as e:
#             assert False, f"An unexpected error occurred: {e}"
#     else:
#         assert False, "Application is not started"


@then('I "{button}" the media playback')
def step_pause_media_playback(context, button):
    if context.app:
        try:
            send_keys('^p')  # Send Ctrl+P to pause/play
        except Exception as e:
            assert False, f"Failed to send pause command: {e}"
    else:
        assert False, "Application is not started"


@then('I full screen the media playback')
def step_full_screen_media(context):
    if context.app:
        try:
            send_keys('%{ENTER}')  # Send Alt+Enter to full screen
        except Exception as e:
            assert False, f"Failed to full screen the media: {e}"
    else:
        assert False, "Application is not started"


@then('I move the volume slider to right')
def step_move_volume_slider(context):
    if context.app:
        try:
            volume_seek_bar = (context.app
                                           .WindowsMediaPlayerLegacy
                                           .child_window(title="Volume", control_type="Slider")
                                           .wrapper_object())

            volume_seek_bar.click_input()
            slider_rect = volume_seek_bar.rectangle()

            # Calculate the midpoint of the slider's vertical position
            y_position = (slider_rect.top + slider_rect.bottom) // 2

            # Initial position
            initial_x = slider_rect.left
            current_x = initial_x

            # Move to the right for 1 second
            end_time = time.time() + 1
            while time.time() < end_time:
                current_x += 1  # Move 1 pixel to the right on each iteration
                mouse.move(coords=(current_x, y_position))
                time.sleep(0.01)  # Small delay to simulate dragging

            # Click to finalize the position
            mouse.click(coords=(current_x, y_position))


        except Exception as e:
            assert False, f"Failed to move volume slider: {e}"
    else:
        assert False, "Application is not started"


@then('I move the volume slider to left')
def step_move_volume_slider(context):
    if context.app:
        try:
            volume_seek_bar = (context.app
                                           .WindowsMediaPlayerLegacy
                                           .child_window(title="Volume", control_type="Slider")
                                           .wrapper_object())

            # Get the current position and dimensions of the slider
            volume_seek_bar.click_input()
            slider_rect = volume_seek_bar.rectangle()

            # Calculate the midpoint of the slider's vertical position
            y_position = (slider_rect.top + slider_rect.bottom) // 2

            # Initial position
            initial_x = slider_rect.left
            current_x = initial_x

            # Move to the left for 1 second
            end_time = time.time() + 1
            while time.time() < end_time:
                current_x -= 1  # Move 1 pixel to the left on each iteration
                mouse.move(coords=(current_x, y_position))
                time.sleep(0.01)  # Small delay to simulate dragging

            # Click to finalize the position
            mouse.click(coords=(current_x, y_position))


        except Exception as e:
            assert False, f"Failed to move volume slider: {e}"
    else:
        assert False, "Application is not started"


@then('I click on the escape button to resize media playback')
def click_on_the_minimize_button(context):
    if context.app:
        try:
            send_keys('{ESC}')

        except ElementNotFoundError as e:
            assert False, f"Element not found: {e}"
        except TimeoutError as e:
            assert False, f"Operation timed out: {e}"
        except Exception as e:
            assert False, f"An unexpected error occurred: {e}"
    else:
        assert False, "Application is not started"



@then('I move the play seek slider to right')
def step_move_slider(context):
    if context.app:
        try:
            volume_seek_bar = (context.app
                                           .WindowsMediaPlayerLegacy
                                           .child_window(title="Seek", control_type="Slider")
                                           .wrapper_object())

            volume_seek_bar.click_input()
            slider_rect = volume_seek_bar.rectangle()

            # Calculate the midpoint of the slider's vertical position
            y_position = (slider_rect.top + slider_rect.bottom) // 2

            # Initial position
            initial_x = slider_rect.left
            current_x = initial_x

            # Move to the right for 1 second
            end_time = time.time() + 1
            while time.time() < end_time:
                current_x += 1  # Move 1 pixel to the right on each iteration
                mouse.move(coords=(current_x, y_position))
                time.sleep(0.01)  # Small delay to simulate dragging

            # Click to finalize the position
            mouse.click(coords=(current_x, y_position))


        except Exception as e:
            assert False, f"Failed to move volume slider: {e}"
    else:
        assert False, "Application is not started"


@then('I move the play seek slider to left')
def step_move_volume_slider(context):
    if context.app:
        try:
            volume_seek_bar = (context.app
                                           .WindowsMediaPlayerLegacy
                                           .child_window(title="Seek", control_type="Slider")
                                           .wrapper_object())

            # Get the current position and dimensions of the slider
            volume_seek_bar.click_input()
            slider_rect = volume_seek_bar.rectangle()

            # Calculate the midpoint of the slider's vertical position
            y_position = (slider_rect.top + slider_rect.bottom) // 2

            # Initial position
            initial_x = slider_rect.left
            current_x = initial_x

            # Move to the left for 1 second
            end_time = time.time() + 1
            while time.time() < end_time:
                current_x -= 1  # Move 1 pixel to the left on each iteration
                mouse.move(coords=(current_x, y_position))
                time.sleep(0.01)  # Small delay to simulate dragging

            # Click to finalize the position
            mouse.click(coords=(current_x, y_position))


        except Exception as e:
            assert False, f"Failed to move volume slider: {e}"
    else:
        assert False, "Application is not started"


@then('I press Ctrl+Shift+C to see subtitle options')
def press_keys(context):
    if context.app:
        try:
            send_keys('^+c')  # Send Alt+Enter to full screen

        except Exception as e:
            assert False, f"Failed to full screen the media: {e}"
    else:
        assert False, "Application is not started"


@then('I press ALT+P, then press B then press F')
def press_keys(context):
    if context.app:
        try:
            send_keys('%P')
            time.sleep(1)  # Wait a bit for the menu to open

            # Send B to select the next item
            send_keys('b')
            time.sleep(0.5)  # Wait a bit for the action to be processed

            # Send F to perform the action
            send_keys('f')
            time.sleep(0.5)  # Wait a bit for the action to be processed

        except Exception as e:
            assert False, f"Failed to full screen the media: {e}"
    else:
        assert False, "Application is not started"
