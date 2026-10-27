import numpy as np


def sigmoid(x):
    """Calculate sigmoid"""
    return 1 / (1 + np.exp(-np.array(x, dtype=float)))


# ─────────────────────────────────────────────
#  SIGMOID NOTEBOOK GRADERS
# ─────────────────────────────────────────────

def grade_h(h, x, w):
    """Grade: linear combination of inputs and weights (h = x · w)"""
    answer = np.dot(x, w)
    if h == answer:
        print("✅ Good job! `h` is correct.")
    else:
        print("❌ Try again. `h` is not correct.")


def grade_nn_output(nn_output, x, w):
    """Grade: sigmoid output of neural network"""
    answer = sigmoid(np.dot(x, w))
    if nn_output == answer:
        print("✅ Good job! `nn_output` is correct.")
    else:
        print("❌ Try again. `nn_output` is not correct.")


def grade_error(error, y, nn_output, x, w):
    """Grade: error = y - nn_output"""
    nn_output_answer = sigmoid(np.dot(x, w))
    answer = y - nn_output_answer
    if error == answer:
        print("✅ Good job! `error` is correct.")
    else:
        print("❌ Try again. `error` is not correct.")


def grade_error_term(error_term, y, x, w):
    """Grade: error_term = error * nn_output * (1 - nn_output)"""
    nn_output_answer = sigmoid(np.dot(x, w))
    error_answer = y - nn_output_answer
    answer = error_answer * nn_output_answer * (1 - nn_output_answer)
    if error_term == answer:
        print("✅ Good job! `error_term` is correct.")
    else:
        print("❌ Try again. `error_term` is not correct.")


def grade_del_w(del_w, learnrate, y, x, w):
    """Grade: weight update = learnrate * error_term * x"""
    nn_output_answer = sigmoid(np.dot(x, w))
    error_answer = y - nn_output_answer
    answer = learnrate * error_answer * nn_output_answer * (1 - nn_output_answer) * x
    if np.array_equal(del_w, answer):
        print("✅ Good job! `del_w` is correct.")
    else:
        print("❌ Try again. `del_w` is not correct.")


# ─────────────────────────────────────────────
#  BACKPROPAGATION NOTEBOOK GRADERS
# ─────────────────────────────────────────────

def grade_output_error(error, target, output):
    """Grade: output error = target - output"""
    answer = target - output
    if error == answer:
        print("✅ Well done! `error` is correct.")
    else:
        print("❌ Try again. `error` is not correct.")


def grade_output_error_term(output_error_term, error, output):
    """Grade: output error term = error * output * (1 - output)"""
    answer = error * output * (1 - output)
    if output_error_term == answer:
        print("✅ Well done! `output_error_term` is correct.")
    else:
        print("❌ Try again. `output_error_term` is not correct.")


def grade_hidden_error_term(hidden_error_term, output_error_term, weights_hidden_output, hidden_layer_output):
    """Grade: hidden error term = (output_error_term · W_ho) * h * (1 - h)"""
    answer = (np.dot(output_error_term, weights_hidden_output)
              * hidden_layer_output * (1 - hidden_layer_output))
    if np.array_equal(hidden_error_term, answer):
        print("✅ Well done! `hidden_error_term` is correct.")
    else:
        print("❌ Try again. `hidden_error_term` is not correct.")


def grade_delta_w_h_o(delta_w_h_o, learnrate, output_error_term, hidden_layer_output):
    """Grade: Δw (hidden→output) = learnrate * output_error_term * hidden_layer_output"""
    answer = learnrate * output_error_term * hidden_layer_output
    if np.array_equal(delta_w_h_o, answer):
        print("✅ Well done! `delta_w_h_o` is correct.")
    else:
        print("❌ Try again. `delta_w_h_o` is not correct.")


def grade_delta_w_i_h(delta_w_i_h, learnrate, hidden_error_term, x):
    """Grade: Δw (input→hidden) = learnrate * hidden_error_term * x (outer product)"""
    answer = learnrate * hidden_error_term * x[:, None]
    if np.array_equal(delta_w_i_h, answer):
        print("✅ Well done! `delta_w_i_h` is correct.")
    else:
        print("❌ Try again. `delta_w_i_h` is not correct.")
